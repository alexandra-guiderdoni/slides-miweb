"""Agrégation des seuls artefacts acceptés du dispatch courant, sans mutation Git."""
import collections
import csv
import datetime
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess

run = Path(__file__).resolve().parent
root = run.parents[3]
results = root / 'visual-tests/_results'
dispatch_path = run / 'dispatch.json'
dispatch = json.loads(dispatch_path.read_text())
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip() == dispatch['base_sha']
zones = []
for entry in dispatch['entries']:
    path = root / entry['artifact']
    zone = json.loads(path.read_text())
    assert all(zone[key] == entry[key] for key in ['run_id', 'base_sha', 'zone_id', 'round', 'agent_id'])
    assert isinstance(zone['bugs'], list)
    entry['status'] = 'completed'
    entry['retention'] = 'Artefact partagé relu et identité validée, sans mutation index Git, selon consigne utilisateur.'
    zones.append(zone)
dispatch['accepted_artifacts'] = [entry['artifact'] for entry in dispatch['entries']]
previous_path = root / dispatch['archived_previous'] / 'audit-results.json'
previous = json.loads(previous_path.read_text()) if previous_path.exists() else {}
key = lambda bug: (bug['file'], ' '.join(bug['title'].lower().split()))
previous_keys = {key(bug) for bug in previous.get('bugs', [])}
bugs = []
seen = set()
for zone in zones:
    for original in zone['bugs']:
        bug = dict(original)
        assert re.fullmatch(r'r\d+-(z\w+|xz)-\d{3}', bug['id'])
        assert (root / bug['file']).is_file()
        assert bug['severity'] in ['critical', 'high', 'medium', 'low']
        assert bug['fix_tier'] in ['mechanical', 'test-first', 'human-only']
        if bug.get('negative_evidence'):
            negative = bug['negative_evidence']
            assert negative['complete'] and negative['scope'] and negative['searches'] and negative['inspected_files']
        assert bug['fix_applied'] is False
        if key(bug) in seen:
            continue
        seen.add(key(bug))
        bug['lifecycle'] = 'persistent' if key(bug) in previous_keys else 'new'
        slug = Path(bug['file']).parts[0]
        bug['impacted_routes'] = ['/' + slug + '/', '/' + slug + '/alternatives.html'] if 'source/' not in bug['file'] else []
        bugs.append(bug)
counts = collections.Counter(bug['severity'] for bug in bugs)
fixes = collections.Counter(bug['fix_tier'] for bug in bugs)
categories = ['security', 'race-condition', 'silent-exception', 'api-guard', 'resource-leak', 'type-mismatch', 'dead-code', 'infra', 'ssr-hydration', 'input-validation', 'error-handling', 'performance', 'accessibility', 'logic-error', 'integration', 'other']
category_counts = collections.Counter(bug['category'] for bug in bugs)
scoped = subprocess.check_output(['git', 'diff', '--name-only', 'c8a7257...HEAD', '--', 'formulaires-opquast-v5/', 'identification-contact-opquast-v5/'], cwd=root, text=True).splitlines()
audited_slugs = {zone['series'] for zone in dispatch['zones']}
comparable = [bug for bug in previous.get('bugs', []) if Path(bug['file']).parts[0] in audited_slugs and 'build.py' not in bug['file']]
fixed_history = [dict(file=bug['file'], title=bug['title'], severity=bug['severity']) for bug in comparable if key(bug) not in seen]
life = collections.Counter(bug['lifecycle'] for bug in bugs)
weights = {'critical': 25, 'high': 15, 'medium': 5, 'low': 1}
risk = round(sum(weight * (0.5 ** index) for index, weight in enumerate(sorted([weights[bug['severity']] for bug in bugs], reverse=True))))
now = datetime.datetime.now(datetime.timezone.utc)
started = datetime.datetime.fromisoformat(dispatch['started_at'])
verification = dict(checked=0, confirmed=0, uncertain=0, rejected=0, skipped=0)
routes = []
for route in sorted({route for bug in bugs for route in bug['impacted_routes']}):
    affected = [bug for bug in bugs if route in bug['impacted_routes']]
    routes.append(dict(route=route, severity=max(affected, key=lambda bug: weights[bug['severity']])['severity'], reason=' ; '.join(bug['title'] for bug in affected), bug_count=len(affected)))
skill = Path('/Users/alex/.codex/plugins/cache/personal/shipguard-codex/2.18.4+codex.local-20261106164932/skills/sg-code-audit')
prompt_material = (skill / 'references/agent-prompt.md').read_text() + (skill / 'references/checklists.md').read_text() + json.dumps(dispatch['zones'], ensure_ascii=False) + 'Contrôle individuel PNG, alt, description, Lecture du visuel, textes_visibles, exercices, personnages. Exclusion générateurs/catalogue.'
report = dict(run_id=dispatch['run_id'], base_sha=dispatch['base_sha'], repo='slides-miweb', timestamp=now.isoformat(), mode='standard', prompt_hash=hashlib.sha256(prompt_material.encode()).hexdigest(), rounds=1, agent_count=len(zones), agents=[dict(id=zone['zone_id'], label=zone['zone'], status='completed', files_audited=zone['files_audited'], bugs_found=len(zone['bugs']), duration_ms=zone['duration_ms'], paths=dispatch['zones'][index]['paths']) for index, zone in enumerate(zones)], scope_info=dict(mode='diff', base_ref='c8a7257', base_sha=dispatch['base_sha'], merge_base_sha=subprocess.check_output(['git', 'merge-base', 'c8a7257', 'HEAD'], cwd=root, text=True).strip(), diff_files=len(scoped), importer_files=0, total_in_scope=len(scoped), files=scoped, exclusions=['Générateurs', 'Catalogue racine'], user_override='PNG, JSON et Markdown inclus à la demande explicite; pas d’expansion vers générateurs/importeurs.'), summary=dict(total_bugs=len(bugs), by_severity={severity:counts[severity] for severity in weights}, by_fix_tier={tier:fixes[tier] for tier in ['mechanical', 'test-first', 'human-only']}, by_category={category:category_counts[category] for category in categories}, files_audited=sum(zone['files_audited'] for zone in zones), files_modified=0, duration_ms=round((now-started).total_seconds()*1000), risk_score=risk, lifecycle=dict(new=life['new'], persistent=life['persistent'], fixed=len(fixed_history), not_rechecked=len(previous.get('bugs', []))-len(comparable), compared_to=previous.get('timestamp'))), impacted_ui_routes=routes, impacted_backend=[], verification=verification, bugs=bugs, unverified_bugs=[], accepted_bugs=[], fixed_since_last_run=fixed_history, execution_notes=dict(model='inherited/unknown', worktrees=False, source_commits=False, audit_mutation=False, correction_phase='Les corrections ultérieures sont suivies dans resolution.json; ce rapport conserve les constats initiaux.', png_reviewed_individually=105, cross_zone='Sans objet en standard : pages statiques, pas de backend dans le périmètre.', negative_evidence_replay='negative-evidence-replay.json', source_files_shared='Les fragments JSON/HTML et les prompts/PNG sont répartis par plages de slides sans chevauchement de contenu.', accepted_risks='Aucun risque accepté trouvé pour ces constats.'))
for target in [run/'audit-results.json', results/'audit-results.json']:
    temporary=target.with_suffix('.json.tmp');temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n');temporary.replace(target)
buffer=io.StringIO();buffer.write('# audit-results.toon\n');buffer.write(f"# run:{report['run_id']} base:{report['base_sha']} repo:slides-miweb mode:standard ts:{report['timestamp']} rounds:1 agents:4\n");buffer.write(f"# scope:diff diff_files:{len(scoped)} total:{len(scoped)}\n");buffer.write(f"# summary: total={len(bugs)} critical={counts['critical']} high={counts['high']} medium={counts['medium']} low={counts['low']}\n");buffer.write('# verified: checked=0 confirmed=0 uncertain=0 rejected=0\n');buffer.write(f'# bugs[{len(bugs)}]{{id,severity,category,fix_tier,file,line,title,verified,score}}:\n');writer=csv.writer(buffer,lineterminator='\n')
for bug in bugs:writer.writerow([bug[name] for name in ['id','severity','category','fix_tier','file','line','title']]+['null','null'])
for target in [run/'audit-results.toon',results/'audit-results.toon']:target.write_text(buffer.getvalue())
dispatch['status']='completed';dispatch['completed_at']=now.isoformat();dispatch['negative_evidence_gate']=dict(checked=2,rejected=0,retained=2);dispatch['source_edits_during_audit']='Aucune par les agents. Parent a corrigé S33 après fin et rétention de z02; autres zones inchangées.';dispatch_path.write_text(json.dumps(dispatch,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False,indent=2))
