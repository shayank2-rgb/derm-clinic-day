import {readdir,readFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {dirname,join} from 'node:path';
const root=dirname(fileURLToPath(import.meta.url));
const folder=join(root,'..','src','data','cases');
const required=['id','demographics','chiefComplaint','lesionSite','hiddenDiagnosis','urgency','historyAnswers','examFindings','image','imageStatus','correctMorphology','acceptableDifferential','tests','acceptableTreatments','unacceptableTreatments','idealDisposition','teachingPearl','traps','needsReview'];
const cases=[];
for(const name of (await readdir(folder)).filter(x=>x.endsWith('.json')&&!['index.json','schema.json'].includes(x))){
  const c=JSON.parse(await readFile(join(folder,name),'utf8'));
  if(required.some(key=>!(key in c)))throw new Error(`Missing required field in ${name}`);
  if(!/^[a-z0-9-]+$/.test(c.id)||!['routine','high','critical'].includes(c.urgency))throw new Error(`Invalid identifier or urgency in ${name}`);
  if(!['real','needs_image'].includes(c.imageStatus)||c.image.status!==c.imageStatus)throw new Error(`Image status mismatch in ${name}`);
  if(!Array.isArray(c.tests)||!Array.isArray(c.correctMorphology)||typeof c.needsReview!=='boolean')throw new Error(`Invalid field type in ${name}`);
  cases.push(c);
}
if(cases.length<30)throw new Error(`Expected at least 30 cases, received ${cases.length}`);
const ids=new Set(cases.map(c=>c.id));if(ids.size!==cases.length)throw new Error('Duplicate case identifiers');
console.log(`Validated ${cases.length} cases; ${cases.filter(c=>c.imageStatus==='real').length} real images, ${cases.filter(c=>c.imageStatus==='needs_image').length} placeholders.`);
