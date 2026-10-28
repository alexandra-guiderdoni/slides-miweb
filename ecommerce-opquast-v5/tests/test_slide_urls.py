"""Régression : les liens directs doivent atteindre aussi les vues 100 à 132."""

import json
import re
import subprocess
import unittest

from test_site_contracts import load_build_module


class SlideUrlsTest(unittest.TestCase):
    def test_direct_links_round_trip_and_reject_invalid_indices(self):
        build = load_build_module()
        html = build.render_v1_index(build.load_slides())
        functions = "\n".join(
            re.search(
                r"function " + name + r"\([^)]*\) \{.*?\n  \}", html, re.DOTALL
            ).group(0)
            for name in ("getIndexFromHash", "slideHash")
        )
        script = "const total=132; const window={location:{hash:''}};\n" + functions
        script += """
const results=[];
for (const index of [0, 8, 98, 99, 105, 131]) {
  window.location.hash=slideHash(index);
  results.push(getIndexFromHash());
}
for (const hash of ['#slide-00', '#slide-133', '#slide-132x', '#other']) {
  window.location.hash=hash;
  results.push(getIndexFromHash());
}
process.stdout.write(JSON.stringify(results));
"""
        result = subprocess.run(
            ["node", "-e", script], capture_output=True, text=True, check=True
        )
        self.assertEqual(
            json.loads(result.stdout), [0, 8, 98, 99, 105, 131, 0, 0, 0, 0]
        )
