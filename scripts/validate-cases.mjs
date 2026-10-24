import {readFile,access} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {dirname,join} from 'node:path';
const root=dirname(fileURLToPath(import.meta.url));
const folder=join(root,'..','src','data','cases');
const imageFolder=join(root,'..','public','images','cases');
const ids=JSON.parse(await readFile(join(folder,'index.json'),'utf8'));
if(!Array.isArray(ids)||ids.length<20||new Set(ids).size!==ids.length)throw new Error('Active case index is missing, too small, or contains duplicate IDs');
const required=['id','demographics','chiefComplaint','lesionSite','hiddenDiagnosis','urgency','historyAnswers','examFindings','image','imageStatus','correctMorphology','acceptableDifferential','tests','acceptableTreatments','unacceptableTreatments','idealDisposition','teachingPearl','traps','needsReview'];
const cases=[];
for(const id of ids){
  if(!/^[a-z0-9-]+$/.test(id))throw new Error(`Invalid case identifier in index: ${id}`);
  const name=`${id}.json`;const c=JSON.parse(await readFile(join(folder,name),'utf8'));
  if(required.some(key=>!(key in c)))throw new Error(`Missing required field in ${name}`);
  if(c.id!==id||!['routine','high','critical'].includes(c.urgency))throw new Error(`Invalid identifier or urgency in ${name}`);
  if(c.imageStatus!=='real'||c.image?.status!=='real')throw new Error(`Playable case ${id} must use a supplied real image`);
  if(!Array.isArray(c.tests)||!Array.isArray(c.correctMorphology)||typeof c.needsReview!=='boolean')throw new Error(`Invalid field type in ${name}`);
  await access(join(imageFolder,c.image.file));cases.push(c);
}
console.log(`Validated ${cases.length} active cases; all have supplied photographs.`);
