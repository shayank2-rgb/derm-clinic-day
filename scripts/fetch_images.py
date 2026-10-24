#!/usr/bin/env python3
"""Fetch only manually approved, traceable source images and write WebP + credits.

Install Pillow first (`python -m pip install Pillow`). Source image license and diagnosis
must be verified on the linked page; inspect for identifiable people before approval.
"""
from datetime import date
from io import BytesIO
import json
from pathlib import Path
from urllib.request import Request, urlopen
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / 'scripts/image_sources.json'
CREDITS = ROOT / 'public/images/credits.json'
OUT = ROOT / 'public/images/cases'
ALLOWED = ('CC0', 'Creative Commons Attribution', 'Creative Commons Attribution-ShareAlike', 'Public Domain')

sources = json.loads(SOURCES.read_text())
credits = json.loads(CREDITS.read_text())
for source in sources:
    if not source.get('approved_for_use'):
        print(f"SKIP {source['case_id']}: source is not visually approved")
        continue
    lic = source['license']
    if not any(lic.startswith(x) for x in ALLOWED) or 'NonCommercial' in lic or 'NoDerivatives' in lic:
        raise SystemExit(f"Refusing disallowed or unclear license: {source['case_id']}")
    req = Request(source['file_url'], headers={'User-Agent':'DermClinicDay/1.0 (educational static game)'})
    with urlopen(req, timeout=30) as response:
        image = Image.open(BytesIO(response.read())).convert('RGB')
    if source.get('crop_box'):
        image = image.crop(tuple(source['crop_box']))
    image.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
    OUT.mkdir(parents=True, exist_ok=True)
    filename = f"{source['case_id']}.webp"
    image.save(OUT / filename, 'WEBP', quality=86, method=6, exif=b'')
    entry = {'file':filename,'caseId':source['case_id'],'sourceSite':source['source_site'],'directPageUrl':source['page_url'],'title':source['title'],'authorOrCredit':source['author'],'licenseName':source['license'],'licenseUrl':source['license_url'],'dateAccessed':date.today().isoformat(),'diagnosisAsStated':source['diagnosis_as_stated'],'fitzpatrickType':None,'modificationsMade':('Cropped to '+str(source['crop_box'])+'; ' if source.get('crop_box') else '')+'Resized to max 1200 px long edge; converted to WebP; metadata stripped.'}
    credits = [c for c in credits if c['file'] != filename] + [entry]
    case_path = ROOT / 'src/data/cases' / f"{source['case_id']}.json"
    case = json.loads(case_path.read_text())
    case['imageStatus']='real'
    case['image']={'file':filename,'status':'real','alt':source.get('alt',f"Open-license teaching image labeled by source as {source['diagnosis_as_stated']}; not the fictional patient's record."),'credit':f"Photo: {source['author']} · {source['license'].replace('Creative Commons Attribution-ShareAlike 4.0 International','CC BY-SA 4.0').replace('Creative Commons Attribution 4.0 International','CC BY 4.0')}"}
    case_path.write_text(json.dumps(case,indent=2)+'\n')
CREDITS.write_text(json.dumps(credits,indent=2)+'\n')
