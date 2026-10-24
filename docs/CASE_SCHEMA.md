# Case data schema

Each case is one JSON file in `src/data/cases/`. Engine behavior reads the shared fields through `src/engine/types.ts`; `src/engine/schema.ts` checks required fields and basic types before cases enter the app.

| Field | Shape | Purpose |
|---|---|---|
| `id` | kebab-case string | Stable case identifier and image filename stem |
| `category` | `common`, `cancer`, or `urgent` | Session balancing and reporting |
| `demographics` | age, sex, pregnancy relevance, context | Fictional patient details |
| `chiefComplaint` | string | Patient-facing opening concern |
| `lesionSite` | string | Explicit anatomical site for the lesion and image alt text |
| `hiddenDiagnosis` | string | Teaching card answer |
| `urgency` | `routine`, `high`, `critical` | Priority and strike rules |
| `historyAnswers` | question-to-answer map | Revealed only when the player asks that question |
| `examFindings` | maneuver-to-finding map | Revealed after each exam maneuver |
| `image` | file, status, alt | Local image or labeled placeholder; `status` is `real` or `needs_image` |
| `imageStatus` | `real` or `needs_image` | Explicit image status used by review and reporting |
| `correctMorphology` | string array | Accepted primary lesion descriptions |
| `acceptableDifferential` | string array | Accepted working diagnosis choices |
| `tests` | name, result, minutes, indicated | Workup menu and value scoring |
| `acceptableTreatments` | name, reason | Safe plan and scoring key |
| `unacceptableTreatments` | name, reason | Penalty and feedback explanations |
| `idealDisposition` | string | Recommended end-of-visit action |
| `teachingPearl` | string | Case-close learning point |
| `traps` | string array | Common reasoning errors |
| `needsReview` | boolean | Specialist review flag; flagged cases are in `docs/REVIEW_CHECKLIST.md` |

Optional `urgentReason` explains why delay matters. Keep stories fictional. Do not put identifying information or real patient narratives in case data. `scripts/generate_cases.py` is the source authoring helper for the initial set; edit the individual JSON case after generation so authored changes are not overwritten.
