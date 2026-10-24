"""Regenerate spoiler-free illustrative SVG cards from the local case files."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CASES=ROOT/'src/data/cases'
OUT=ROOT/'public/images/cases'
OUT.mkdir(parents=True,exist_ok=True)
for path in sorted(CASES.glob('*.json')):
    if path.name in ('index.json','schema.json'): continue
    case=json.loads(path.read_text())
    site=case.get('lesionSite') or case['chiefComplaint'].rsplit(' on ',1)[-1]
    image={'file':case['id']+'.svg','status':'needs_image','alt':f'Original vector placeholder, not a clinical photograph: a generic abstract lesion swatch, site {site}. No patient or diagnosis is depicted.'}
    case['image']=image
    case['imageStatus']='needs_image'
    path.write_text(json.dumps(case,indent=2)+'\n')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 480" role="img" aria-labelledby="title desc"><title id="title">Illustrative skin finding placeholder</title><desc id="desc">Original schematic vector, not a patient photograph. Abstract skin swatch at {site}; no diagnosis or skin tone is asserted.</desc><defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#f2eee7"/><stop offset="1" stop-color="#e4e8e2"/></linearGradient><linearGradient id="skin"><stop stop-color="#a9684f"/><stop offset=".48" stop-color="#c88d6d"/><stop offset="1" stop-color="#dfb99b"/></linearGradient></defs><rect width="800" height="480" rx="28" fill="url(#bg)"/><rect x="45" y="44" width="710" height="392" rx="20" fill="#fff" opacity=".82"/><text x="78" y="100" fill="#26483f" font-family="Arial,sans-serif" font-size="20" font-weight="700" letter-spacing="2">TEACHING VISUAL</text><rect x="78" y="130" width="290" height="230" rx="30" fill="url(#skin)"/><path d="M160 233c12-37 47-51 81-38 24 9 32 34 52 40-8 31-27 48-63 50-37 2-65-18-70-52Z" fill="#9a514f" opacity=".88"/><path d="M174 231c15-18 32-25 49-25 22 0 34 17 53 24" fill="none" stroke="#f0c9a8" stroke-width="8" stroke-linecap="round" opacity=".8"/><text x="405" y="187" fill="#1d342e" font-family="Arial,sans-serif" font-size="28" font-weight="700">Illustrative lesion</text><text x="405" y="229" fill="#4a5c55" font-family="Arial,sans-serif" font-size="18">Site: {site}</text><text x="405" y="270" fill="#4a5c55" font-family="Arial,sans-serif" font-size="16">Schematic cue — not clinical photography</text><text x="405" y="308" fill="#4a5c55" font-family="Arial,sans-serif" font-size="16">No diagnosis, skin tone, or type is inferred.</text><rect x="78" y="382" width="644" height="32" rx="16" fill="#e9f0ed"/><text x="98" y="404" fill="#26483f" font-family="Arial,sans-serif" font-size="14" font-weight="700">PLACEHOLDER · replace only with verified, credited open-license image</text></svg>'''
    (OUT/(case['id']+'.svg')).write_text(svg)
print(f'Generated {len(list(CASES.glob("*.json")))-2} spoiler-free SVG placeholders.')
