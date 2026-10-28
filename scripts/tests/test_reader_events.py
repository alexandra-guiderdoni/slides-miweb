"""Exécute les gestionnaires réels des lecteurs dans un contexte JavaScript isolé avec Node."""
import ast
import json
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]


def reader_script(path):
    tree = ast.parse(path.read_text())
    return next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "MAIN_JS" for t in node.targets))


class ReaderEventsTest(unittest.TestCase):
    def test_skip_fragments_preserve_position_and_history_restores_slides(self):
        for path in sorted(ROOT.glob("*/build.py")):
            if 'window.addEventListener("popstate"' not in path.read_text():
                continue
            with self.subTest(reader=path.parent.name):
                source = reader_script(path)
                functions = "\n".join(re.search(r"  function " + name + r"\([^)]*\) \{.*?\n  \}", source, re.S).group()
                                      for name in ("getIndexFromHash", "isAllSlidesRequested"))
                handler = re.search(r'  window.addEventListener\("popstate",.*?\n  \}\);', source, re.S).group()
                script = """
const assert=require('node:assert/strict');
const total=132; let currentIndex=59, allMode=false, calls=0, listener;
const window={location:{hash:'#slide-60',search:''},history:{state:null,replaceState(state){this.state=state;}},addEventListener:(name,fn)=>listener=fn};
function showSlide(index){currentIndex=index;allMode=false;calls++;}
function showAllSlides(){allMode=true;calls++;}
""" + functions + "\n" + handler + """
for(const hash of ['#contenu','#sommaire','#diaporama','#description-active','#footer']) {
 window.history.state=null; window.location.hash=hash; listener();
 assert.equal(currentIndex,59);assert.equal(calls,0);assert.equal(window.location.hash,hash);
}
const anchorState=window.history.state;
window.location.hash='#slide-132';listener();assert.equal(currentIndex,131);
window.location.search='?slides=all';window.location.hash='#diaporama';listener();assert.equal(allMode,true);
window.location.search='';window.location.hash='#sommaire';window.history.state=anchorState;listener();assert.equal(currentIndex,59);assert.equal(allMode,false);assert.equal(window.location.hash,'#sommaire');
window.location.hash='#slide-60';listener();assert.equal(currentIndex,59);assert.equal(allMode,false);
"""
                result = subprocess.run(["node", "-e", script], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_keyboard_navigation_is_scoped_to_reader(self):
        for slug in ("matrice-slide-ai", "ecommerce-opquast-v5"):
            with self.subTest(reader=slug):
                source = reader_script(ROOT / slug / "build.py")
                handler = re.search(r'  document.addEventListener\("keydown",.*?\n  \}\);', source, re.S).group()
                script = """
const assert=require('node:assert/strict');let listener, currentIndex=59, allMode=false, prevented=false;
const total=132;const document={addEventListener:(name,fn)=>listener=fn};
const fullscreenTarget={contains:target=>target.inside};function isProjectionActive(){return false;}
function showSlide(index){currentIndex=index;}
function key(inside,editing=false){prevented=false;listener({key:'End',target:{inside,isContentEditable:editing,tagName:'DIV',closest:()=>editing?{}:null},preventDefault:()=>prevented=true});}
""" + handler + """
key(false);assert.equal(currentIndex,59);assert.equal(prevented,false);
key(true,true);assert.equal(currentIndex,59);assert.equal(prevented,false);
key(true);assert.equal(currentIndex,131);assert.equal(prevented,true);
currentIndex=59;allMode=true;key(true);assert.equal(currentIndex,59);assert.equal(prevented,false);
"""
                result = subprocess.run(["node", "-e", script], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
