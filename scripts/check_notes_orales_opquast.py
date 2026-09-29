#!/usr/bin/env python3
"""Contrôle structurel des notes orales d'une série de slides Opquast."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "numero",
    "titre",
    "image",
    "alt",
    "description",
    "textes_visibles",
    "message",
    "transcription",
    "notes_orateur",
)

FORBIDDEN_HEADINGS = {
    "intention pédagogique",
    "animation",
    "mise en perspective",
    "développement oral",
    "synthèse orale",
    "objectif pédagogique",
}

META_PATTERNS = (
    (re.compile(r"\bobjectif de la slide\b", re.IGNORECASE), "objectif de slide"),
    (re.compile(r"\bconsigne au présentateur\b", re.IGNORECASE), "consigne au présentateur"),
    (re.compile(r"\bdemandez au groupe\b", re.IGNORECASE), "gestion du groupe"),
    (re.compile(r"\binvitez le groupe\b", re.IGNORECASE), "gestion du groupe"),
    (re.compile(r"\bles participants\b", re.IGNORECASE), "gestion des participants"),
    (re.compile(r"\bcommentez le visuel\b", re.IGNORECASE), "consigne sur le visuel"),
    (re.compile(r"\blisez la citation\b", re.IGNORECASE), "consigne de lecture"),
    (re.compile(r"\bmettez en (?:avant|évidence)\b", re.IGNORECASE), "consigne au présentateur"),
    (re.compile(r"\bs[’']appuyer sur le mémo\b", re.IGNORECASE), "consigne au présentateur"),
    (re.compile(r"\bla slide suivante\b", re.IGNORECASE), "commentaire sur le support"),
    (re.compile(r"\bcette slide\b", re.IGNORECASE), "commentaire sur le support"),
    (
        re.compile(r"\b(?:dans ce module|ce module|le module de formation)\b", re.IGNORECASE),
        "commentaire sur le module",
    ),
    (re.compile(r"\ble bloc suivant\b", re.IGNORECASE), "commentaire sur le déroulé"),
    (re.compile(r"\bla séquence suivante\b", re.IGNORECASE), "commentaire sur le déroulé"),
)

RULE_TITLE_RE = re.compile(r"^règle(?:\s+n[°o])?\s+\d+\b", re.IGNORECASE)
RULE_BADGE_RE = re.compile(r"^règle(?:\s+n[°o])?\s+\d+\b", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
BULLET_RE = re.compile(r"^-\s+\S", re.MULTILINE)


@dataclass(frozen=True)
class Issue:
    severity: str
    slide: str
    message: str


def plain_text(value: str) -> str:
    value = re.sub(r"^#{1,6}\s+", "", value, flags=re.MULTILINE)
    value = re.sub(r"^-\s+", "", value, flags=re.MULTILINE)
    value = re.sub(r"^\d+\.\s+", "", value, flags=re.MULTILINE)
    return re.sub(r"\s+", " ", value).strip()


def slide_label(slide: dict[str, Any], position: int) -> str:
    numero = slide.get("numero")
    if isinstance(numero, int) and not isinstance(numero, bool):
        return f"slide {numero}"
    return f"entrée {position}"


def is_rule_slide(slide: dict[str, Any]) -> bool:
    title = slide.get("titre")
    if isinstance(title, str) and RULE_TITLE_RE.search(title.strip()):
        return True
    visible_texts = slide.get("textes_visibles")
    if isinstance(visible_texts, list):
        return any(
            isinstance(text, str) and RULE_BADGE_RE.search(text.strip())
            for text in visible_texts
        )
    return False


def validate_slides(data: Any) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(data, list) or not data:
        return [Issue("ERREUR", "fichier", "slides.json doit contenir une liste non vide.")]

    numbers: list[int] = []
    for position, slide in enumerate(data, start=1):
        if not isinstance(slide, dict):
            issues.append(Issue("ERREUR", f"entrée {position}", "la slide doit être un objet JSON."))
            continue

        label = slide_label(slide, position)
        missing_fields = [field for field in REQUIRED_FIELDS if field not in slide]
        if missing_fields:
            issues.append(
                Issue(
                    "ERREUR",
                    label,
                    "champs manquants : " + ", ".join(missing_fields) + ".",
                )
            )

        numero = slide.get("numero")
        if isinstance(numero, int) and not isinstance(numero, bool):
            numbers.append(numero)

        notes = slide.get("notes_orateur")
        transcription = slide.get("transcription")
        if not isinstance(notes, str) or not notes.strip():
            issues.append(Issue("ERREUR", label, "notes_orateur est absent ou vide."))
            continue

        first_line = next((line.strip() for line in notes.splitlines() if line.strip()), "")
        if not first_line.startswith("### "):
            issues.append(Issue("ERREUR", label, "les notes doivent commencer par un titre de niveau 3."))

        for hashes, heading in HEADING_RE.findall(notes):
            if len(hashes) not in (3, 4):
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        f"niveau de titre interdit : {hashes} {heading}.",
                    )
                )
            if heading.strip().casefold() in FORBIDDEN_HEADINGS:
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        f"titre métapédagogique interdit : {heading}.",
                    )
                )

        for pattern, description in META_PATTERNS:
            match = pattern.search(notes)
            if match:
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        f"métapédagogie détectée ({description}) : {match.group(0)}.",
                    )
                )

        if "–" in notes or "—" in notes:
            issues.append(
                Issue(
                    "ERREUR",
                    label,
                    "un tiret long est présent ; utiliser uniquement le tiret simple.",
                )
            )

        bullet_count = len(BULLET_RE.findall(notes))
        if bullet_count == 0:
            issues.append(Issue("ERREUR", label, "aucune liste à puces n’est présente."))
        elif bullet_count < 4:
            issues.append(
                Issue(
                    "AVERTISSEMENT",
                    label,
                    f"seulement {bullet_count} puce(s) ; vérifier la lisibilité au scan.",
                )
            )

        if is_rule_slide(slide):
            if "#### Impact du non-respect" not in notes:
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        "la section « Impact du non-respect » est absente.",
                    )
                )
            if "#### Ce que garantit la règle" not in notes:
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        "la section « Ce que garantit la règle » est absente.",
                    )
                )

        is_last = position == len(data)
        has_conclusion = "### Conclusion" in notes
        if not is_last and "### Transition" not in notes and not has_conclusion:
            issues.append(Issue("ERREUR", label, "la section « Transition » est absente."))
        if is_last and "### Conclusion" not in notes:
            issues.append(Issue("ERREUR", label, "la dernière slide doit contenir une conclusion."))

        if isinstance(transcription, str) and transcription.strip():
            if plain_text(notes) == plain_text(transcription):
                issues.append(
                    Issue(
                        "ERREUR",
                        label,
                        "le discours oral répète exactement la transcription.",
                    )
                )

    if len(numbers) != len(set(numbers)):
        issues.append(Issue("ERREUR", "fichier", "des numéros de slide sont dupliqués."))
    if numbers and numbers != list(range(1, len(data) + 1)):
        issues.append(
            Issue(
                "ERREUR",
                "fichier",
                "les numéros de slide doivent former une suite commençant à 1.",
            )
        )

    return issues


def load_slides(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"fichier absent : {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"JSON invalide dans {path} : ligne {error.lineno}, colonne {error.colno}"
        ) from error


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage : scripts/check_notes_orales_opquast.py <dossier-jeu>", file=sys.stderr)
        return 2

    slides_path = Path(argv[1]) / "slides.json"
    try:
        data = load_slides(slides_path)
    except ValueError as error:
        print(f"ERREUR fichier : {error}", file=sys.stderr)
        return 2

    issues = validate_slides(data)
    errors = [issue for issue in issues if issue.severity == "ERREUR"]
    warnings = [issue for issue in issues if issue.severity == "AVERTISSEMENT"]

    for issue in issues:
        print(f"{issue.severity} {issue.slide} : {issue.message}")

    slide_count = len(data) if isinstance(data, list) else 0
    print(
        f"Résumé : {slide_count} slide(s), {len(errors)} erreur(s), "
        f"{len(warnings)} avertissement(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
