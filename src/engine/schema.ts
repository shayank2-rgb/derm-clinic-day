import type { CaseFile } from './types';
export const REQUIRED_CASE_FIELDS = ['id','demographics','chiefComplaint','lesionSite','hiddenDiagnosis','urgency','historyAnswers','examFindings','image','imageStatus','correctMorphology','acceptableDifferential','tests','acceptableTreatments','unacceptableTreatments','idealDisposition','teachingPearl','traps','needsReview'] as const;
export function validateCase(value: unknown): value is CaseFile {
  if (!value || typeof value !== 'object') return false;
  const c=value as Record<string, unknown>;
  if (REQUIRED_CASE_FIELDS.some(k => !(k in c))) return false;
  if (typeof c.id!=='string' || !/^[a-z0-9-]+$/.test(c.id)) return false;
  if (!['routine','high','critical'].includes(String(c.urgency))) return false;
  if (!c.demographics || typeof c.demographics!=='object') return false;
  if (!c.historyAnswers || typeof c.historyAnswers!=='object' || !c.examFindings || typeof c.examFindings!=='object') return false;
  if (!c.image || typeof c.image!=='object' || !['real','needs_image'].includes(String(c.imageStatus)) || !Array.isArray(c.correctMorphology) || !Array.isArray(c.tests) || !Array.isArray(c.acceptableTreatments) || !Array.isArray(c.unacceptableTreatments) || !Array.isArray(c.traps)) return false;
  return typeof c.needsReview==='boolean' && typeof c.hiddenDiagnosis==='string' && typeof c.lesionSite==='string' && typeof c.teachingPearl==='string';
}
