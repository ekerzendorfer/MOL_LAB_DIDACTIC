"""V0.9a: model geometry, EN arrows, isolated opt-in and JS overlay lifecycle."""
import contextlib
import html
import io
import json
import math
import re
import subprocess
from pathlib import Path
from IPython.display import HTML
import ipywidgets as widgets
from rdkit import Chem

root=Path(__file__).resolve().parents[1]
nb=json.loads((root/"MOL_LAB_DIDACTIC_v0_4_2.ipynb").read_text(encoding="utf-8"))
source=next("".join(c["source"]) for c in nb["cells"] if "def dipole_learning_payload(" in "".join(c["source"]))
ns={"__name__":"__dipole_v09a_regression__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(source,"DIDACTIC main cell","exec"),ns)
assert ns["DIPOLE_SETS"]["basis"]["members"]==["co2","h2o","nh3","ch4"]
assert [k for k,v in ns["DIPOLE_CASES"].items() if v["ready"]]==["co2","h2o"]
mol=Chem.MolFromSmiles("O")
m3=ns["make_3d"](mol)
card=ns["card_for"]("Polarität und Löslichkeit","Wasser")
assert ns["dipole_case_id"]("Polarität und Löslichkeit",card,mol)=="h2o"
assert ns["dipole_case_id"]("Isomerie",card,mol) is None
assert ns["dipole_case_id"]("Polarität und Löslichkeit",card,mol,True) is None
assert ns["dipole_case_id"]("Polarität und Löslichkeit",{"name":"Methanol"},Chem.MolFromSmiles("CO")) is None
p=ns["dipole_learning_payload"](m3,"h2o")
assert sorted((a["symbol"],a["en"]) for a in p["labels"])==[("H",2.2),("H",2.2),("O",3.44)]
assert len(p["bonds"])==2
for b in p["bonds"]:
    assert (b["low"],b["high"],b["delta_en"])==("H","O",1.24)
    u=tuple(b["direction"].values())
    arrow=tuple(b["end"][k]-b["start"][k] for k in ("x","y","z"))
    assert math.isclose(sum(x*x for x in u),1,abs_tol=1e-10)
    assert all(math.isclose(x,.86*y,abs_tol=1e-10) for x,y in zip(arrow,u))
    cross=tuple(b["cross_b"][k]-b["cross_a"][k] for k in ("x","y","z"))
    assert abs(sum(x*y for x,y in zip(cross,u)))<1e-10
conf=m3.GetConformer()
o=next(a.GetIdx() for a in m3.GetAtoms() if a.GetSymbol()=="O")
expected=[ns["_dip_unit"](ns["_dip_vsub"](tuple(conf.GetAtomPosition(o)),tuple(conf.GetAtomPosition(a.GetIdx()))))
          for a in m3.GetAtoms() if a.GetSymbol()=="H"]
for u in expected:
    assert any(all(math.isclose(x,y,abs_tol=1e-10) for x,y in zip(u,b["direction"].values())) for b in p["bonds"])
for k in ("nh3","ch4"):
    try: ns["dipole_learning_payload"](m3,k)
    except ValueError: pass
    else: raise AssertionError("unready case accepted")

visual=[]
ns["display"]=lambda *items:visual.extend(items)
with contextlib.redirect_stdout(io.StringIO()):
    ns["module_dd"].value="Polarität und Löslichkeit"
    ns["example_dd"].value="Wasser"
    ns["run_btn"].click()
def find_launcher():
    return [x for x in visual if isinstance(x,widgets.VBox) and len(x.children)==2
            and isinstance(x.children[0],widgets.Button)
            and x.children[0].description=="Bindungsdipole untersuchen"]
launchers=find_launcher()
assert len(launchers)==1
button,panel=launchers[0].children
assert not panel.value
button.click()
assert "dipole-learning-frame" in panel.value
inner=html.unescape(re.search(r"srcdoc='(.*?)' width=",panel.value,re.S).group(1))
assert "3dmol@2.5.5" in inner
assert "keine Debye-Werte" in inner
assert "ΔEN = 1,24" in inner
script=re.findall(r"<script>(.*?)</script>",inner,re.S)[0]
# Exercise the real authored JS against a minimal viewer/DOM mock.
# This is NOT a WebGL or Colab visual test.
harness="""const assert=require('node:assert/strict');
const els={};const calls={model:0,zoomTo:0,zoom:0,render:0};
const activeLabels=new Set(),activeShapes=new Set();
function get(id){return els[id]||(els[id]={disabled:true,textContent:'',attrs:{},events:{},setAttribute(k,v){this.attrs[k]=v},addEventListener(k,f){this.events[k]=f}})}
global.document={getElementById:get};
global.window={addEventListener(){},setTimeout(){}};
const viewer={addModel(){calls.model++},setStyle(){},zoomTo(){calls.zoomTo++},zoom(){calls.zoom++},render(){calls.render++},resize(){},
addLabel(t,s){const x={t,s};activeLabels.add(x);return x},removeLabel(x){assert(activeLabels.delete(x))},
addArrow(s){const x={type:'arrow',s};activeShapes.add(x);return x},
addCylinder(s){const x={type:'cross',s};activeShapes.add(x);return x},addSphere(s){const x={type:'sphere',s};activeShapes.add(x);return x},removeShape(x){assert(activeShapes.delete(x))}};
global.$3Dmol={createViewer(){return viewer}};
"""
checks="""assert.equal(calls.model,1);assert.equal(calls.zoomTo,1);assert.equal(activeLabels.size,0);
function click(k){const b=get('dip-stage-'+k);assert(!b.disabled);b.events.click();}
click(1);assert.equal(activeLabels.size,3);assert.equal(activeShapes.size,0);
click(2);assert.equal(activeLabels.size,3);assert.equal(activeShapes.size,4);
assert.equal([...activeShapes].filter(x=>x.type==='arrow').length,2);
assert.equal(get('dip-stage-2').attrs['aria-pressed'],'true');
click(0);assert.equal(activeLabels.size,0);assert.equal(activeShapes.size,0);
click(2);click(1);assert.equal(activeLabels.size,3);assert.equal(activeShapes.size,0);
click(3);assert.equal(activeLabels.size,0);assert.equal(activeShapes.size,1);
get('dip-next').events.click();assert.equal(activeShapes.size,2);
get('dip-next').events.click();assert.equal(activeShapes.size,3);
get('dip-next').events.click();assert.equal(activeShapes.size,1);
assert.equal(get('dip-next').disabled,true);
get('dip-prev').events.click();assert.equal(activeShapes.size,3);
click(0);assert.equal(activeShapes.size,0);assert.equal(get('dip-add-controls').hidden,true);
assert.equal(calls.model,1);assert.equal(calls.zoomTo,1);assert.equal(calls.zoom,1);
console.log('Dipole JS overlays: OK');
"""
subprocess.run(["node","-e",harness+script+checks],check=True)
button.click()
assert panel.value==""
visual.clear()
with contextlib.redirect_stdout(io.StringIO()):
    ns["example_dd"].value="Methanol"
    ns["run_btn"].click()
assert not find_launcher()
visual.clear()
with contextlib.redirect_stdout(io.StringIO()):
    ns["polar_pair_dd"].value="Wasser vs. Schwefelwasserstoff"
assert not find_launcher()
print("V0.9a: water geometry and EN arrows, isolated lazy widget, JS lifecycle – OK")

# V0.9b: check the exact head-to-tail construction and the zero case.
def xyz(p):return tuple(p[k] for k in ("x","y","z"))
def close(a,b):return all(math.isclose(x,y,abs_tol=1e-8) for x,y in zip(a,b))
for cid,smiles in (("h2o","O"),("co2","O=C=O")):
    m=ns["make_3d"](Chem.MolFromSmiles(smiles))
    before=Chem.MolToMolBlock(m)
    payload=ns["dipole_learning_payload"](m,cid)
    assert Chem.MolToMolBlock(m)==before
    points=list(map(xyz,payload["points"]))
    for i,b in enumerate(payload["bonds"]):
        assert close(ns["_dip_vsub"](points[i+1],points[i]),ns["_dip_vscale"](xyz(b["direction"]),.86))
    assert close(ns["_dip_vsub"](xyz(payload["result_end"]),xyz(payload["result_start"])),ns["_dip_vsub"](points[-1],points[0]))
    assert payload["zero"]==(cid=="co2")
    if cid=="h2o":
        assert 1.0<payload["sum_norm"]<1.4
        start,end=xyz(payload["result_start"]),xyz(payload["result_end"])
        u=ns["_dip_unit"](ns["_dip_vsub"](end,start))
        conf=m.GetConformer()
        for atom in m.GetAtoms():
            pos=tuple(conf.GetAtomPosition(atom.GetIdx()))
            radial=ns["_dip_vsub"](pos,start)
            transverse=ns["_dip_vsub"](radial,ns["_dip_vscale"](u,ns["_dip_dot"](radial,u)))
            assert math.sqrt(ns["_dip_dot"](transverse,transverse))>=.60-1e-8
        # The drawn vector stays parallel and equal to the construction.
        # Only the last stage's position changes, not the first three steps.
        assert not close(start,points[0])
    else:
        assert payload["idealized"] and payload["sum_norm"]==0
        assert close(points[0],points[-1])
        assert all(b["low"]=="C" and b["delta_en"]==.89 for b in payload["bonds"])
        card=ns["card_for"]("Polarität und Löslichkeit","Kohlenstoffdioxid")
        assert ns["dipole_case_id"]("Polarität und Löslichkeit",card,Chem.MolFromSmiles(smiles))=="co2"
        frame=ns["dipole_learning_iframe"](m,cid)
        inner=html.unescape(re.search(r"srcdoc='(.*?)' width=",frame,re.S).group(1))
        script=re.findall(r"<script>(.*?)</script>",inner,re.S)[0]
        zero_checks="""function click(k){get('dip-stage-'+k).events.click();}
click(3);assert.equal(activeShapes.size,1);
get('dip-next').events.click();assert.equal(activeShapes.size,2);
get('dip-next').events.click();assert.equal(activeShapes.size,3);assert.equal(activeLabels.size,1);
assert.equal([...activeShapes].filter(x=>x.type==='arrow'&&x.s.color==='#17814a').length,0);
get('dip-next').events.click();assert.equal(activeShapes.size,0);assert.equal(activeLabels.size,1);
assert.equal(calls.model,1);assert.equal(calls.zoomTo,1);
get('dip-prev').events.click();assert.equal(activeShapes.size,3);
click(0);assert.equal(activeShapes.size,0);assert.equal(activeLabels.size,0);
console.log('CO2 zero-sum overlays: OK');"""
        subprocess.run(["node","-e",harness+script+zero_checks],check=True)
print("V0.9b: head-to-tail vectors, idealized CO2 symmetry and reversible overlay lifecycle – OK")
