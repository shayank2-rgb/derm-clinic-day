import json
from pathlib import Path
cases = [
('acne-vulgaris','Acne vulgaris','common','comedones and inflammatory papules on face and upper trunk','comedone','adapalene and benzoyl peroxide; assess pregnancy plans before retinoid counseling','topical retinoid + benzoyl peroxide','discharge'),
('atopic-dermatitis','Atopic dermatitis','common','itchy flexural plaques with chronic relapsing course','plaque','emollients and site-appropriate topical corticosteroid; avoid prolonged potent steroid on folds','topical corticosteroid by site + barrier care','discharge'),
('plaque-psoriasis','Plaque psoriasis','common','well-demarcated plaques with adherent scale on extensor surfaces','plaque','topical corticosteroid with site and duration counseling; assess joints','topical corticosteroid + emollient','discharge'),
('seborrheic-dermatitis','Seborrheic dermatitis','common','greasy scale in scalp and central face','scale','topical antifungal and gentle skin care','topical antifungal','discharge'),
('tinea-corporis','Tinea corporis','common','annular plaque with peripheral scale and central clearing','plaque','confirm with KOH when uncertain; topical antifungal; avoid steroid monotherapy','topical antifungal','discharge'),
('verruca-vulgaris','Verruca vulgaris','common','rough hyperkeratotic papules with interrupted skin lines','papule','observation, salicylic acid, or cryotherapy after counseling','salicylic acid or cryotherapy','discharge'),
('molluscum-contagiosum','Molluscum contagiosum','common','small pearly umbilicated papules in a child','papule','reassurance and observation; discuss autoinoculation and avoid traumatic treatment','observation + education','discharge'),
('rosacea','Papulopustular rosacea','common','central facial erythema and papules without comedones','papule','trigger reduction and topical metronidazole or ivermectin; assess ocular symptoms','topical rosacea therapy + trigger counseling','discharge'),
('hidradenitis-suppurativa','Hidradenitis suppurativa','common','recurrent painful nodules and tunnels in intertriginous skin','nodule','stage disease, discuss smoking/weight without blame, topical or systemic plan by severity','topical clindamycin for limited disease + longitudinal plan','discharge'),
('acute-urticaria','Acute urticaria','common','transient migratory wheals lasting less than a day per lesion','wheal','non-sedating H1 antihistamine; assess airway and anaphylaxis','non-sedating antihistamine','discharge'),
('allergic-contact-dermatitis','Allergic contact dermatitis','common','pruritic eczematous plaques with exposure-shaped borders','plaque','remove exposure; site-appropriate anti-inflammatory therapy; patch testing if recurrent','avoidance + site-appropriate topical corticosteroid','discharge'),
('irritant-contact-dermatitis','Irritant contact dermatitis','common','burning fissured eczematous hands after wet work','patch','barrier protection and emollients; reduce irritant exposure','barrier care + emollients','discharge'),
('tinea-pedis','Tinea pedis','common','interdigital scale and maceration','scale','KOH if uncertain; topical antifungal and moisture control','topical antifungal','discharge'),
('seborrheic-keratosis','Seborrheic keratosis','common','stuck-on waxy papule with comedo-like openings','papule','reassure if typical; biopsy if atypical or changing','reassurance','discharge'),
('androgenetic-alopecia','Androgenetic alopecia','common','patterned nonscarring hair thinning with preserved follicular openings','patch','discuss topical minoxidil; review pregnancy considerations and expectations','topical minoxidil counseling','discharge'),
('onychomycosis','Onychomycosis','common','distal nail thickening and subungual debris','scale','confirm fungus before oral therapy; review liver and medication risks','topical therapy or confirmed-disease systemic plan','discharge'),
('actinic-keratosis','Actinic keratosis','cancer','rough gritty papule on chronically sun-exposed scalp','papule','cryotherapy or field therapy; biopsy if thick, tender, or indurated','cryotherapy','discharge'),
('basal-cell-carcinoma','Basal cell carcinoma','cancer','slow-growing pearly papule with arborizing vessels and focal ulceration','papule','biopsy then definitive surgery; prioritize high-risk sites','biopsy then Mohs or excision by risk','refer'),
('cutaneous-squamous-cell-carcinoma','Cutaneous squamous cell carcinoma','cancer','rapidly growing tender hyperkeratotic nodule on sun-exposed skin','nodule','biopsy and prompt risk-based definitive treatment','biopsy then excision or Mohs by risk','refer'),
('melanoma','Melanoma','cancer','asymmetric evolving pigmented lesion with color variation','patch','urgent complete diagnostic biopsy with appropriate margins; stage after pathology','urgent biopsy and expedited specialist pathway','refer'),
('atypical-nevus','Atypical nevus','cancer','irregularly pigmented macule with asymmetry compared with signature nevi','macule','document and biopsy lesions with concerning evolution or discordance','photodocument or biopsy based on concern','discharge'),
('lentigo-maligna','Lentigo maligna','cancer','slowly enlarging irregularly pigmented macule on sun-damaged face','patch','biopsy representative areas and refer for definitive margin-controlled care','biopsy + specialist referral','refer'),
('early-sjs-ten','Early SJS/TEN','urgent','skin pain, dusky macules, oral erosions, and new medication exposure','macule','stop suspected culprit and send urgently to ED/admission for multidisciplinary care','immediate emergency referral; stop suspected culprit with treating team','ED'),
('dress','DRESS','urgent','new medication, facial edema, morbilliform eruption, fever, and systemic symptoms','patch','urgent hospital evaluation and organ injury labs; coordinate culprit drug discontinuation','urgent ED/admission and multidisciplinary evaluation','ED'),
('pemphigus-vulgaris','Pemphigus vulgaris','urgent','flaccid bullae and painful oral erosions with positive Nikolsky sign','bulla','biopsy lesional and perilesional skin for H&E and DIF; urgent specialist care','urgent dermatology referral + biopsy with DIF','refer'),
('bullous-pemphigoid','Bullous pemphigoid','urgent','tense pruritic bullae in an older adult with negative Nikolsky sign','bulla','lesional biopsy and perilesional DIF; review medications and comorbidity','biopsy with DIF + specialist-directed treatment','refer'),
('dermatomyositis','Dermatomyositis','urgent','heliotrope change, Gottron papules, proximal weakness, and photosensitive eruption','papule','assess muscle and swallowing/respiratory symptoms; coordinated malignancy and myositis evaluation','urgent coordinated specialty evaluation','refer'),
('cutaneous-lupus','Cutaneous lupus erythematosus','common','photosensitive scaly plaques with dyspigmented scarring','plaque','photoprotection, biopsy/labs when indicated, and assess systemic symptoms','photoprotection + specialist follow-up','refer'),
('mycosis-fungoides','Mycosis fungoides','urgent','persistent patch-stage plaques in bathing-trunk distribution despite eczema therapy','patch','repeat biopsies from representative sites; stop topical therapy before biopsy per specialist plan','repeat biopsy + expedited dermatology follow-up','refer'),
('necrotizing-infection','Necrotizing soft-tissue infection','urgent','rapidly progressive pain out of proportion, fever, and dusky skin','patch','immediate emergency surgical evaluation; do not delay for dermatology testing','immediate ED and surgical consultation','ED'),
('calciphylaxis','Calciphylaxis','urgent','exquisitely painful retiform purpura and necrosis in dialysis patient','patch','urgent hospital multidisciplinary care; biopsy only after risk-benefit discussion','urgent admission + nephrology and wound care','ED'),
('drug-eruption','Morbilliform drug eruption','common','symmetric morbilliform rash after a new medication without mucosal or systemic features','patch','review timing and red flags; medication plan coordinated with prescriber','culprit assessment + supportive care / escalation if red flags','discharge'),
('stasis-dermatitis','Stasis dermatitis','common','bilateral lower-leg scale and edema with hemosiderin change','patch','compression after arterial assessment, elevation, emollients; avoid antibiotics absent infection','compression and barrier care after vascular assessment','discharge'),
('scabies','Scabies','common','intensely itchy papules and burrows in finger webs with household itch','papule','permethrin for patient and close contacts with environmental instructions; repeat per protocol','permethrin + contact and linen instructions','discharge'),
('impetigo','Impetigo','common','honey-colored crusted superficial erosions around the nose','crust','hygiene and topical or oral antibiotic based on extent and local guidance','localized topical antimicrobial + hygiene','discharge'),
('alopecia-areata','Alopecia areata','common','well-circumscribed nonscarring patch of hair loss with exclamation point hairs','patch','explain autoimmune course; consider intralesional corticosteroid for limited adult disease','observation or intralesional therapy by site and age','discharge'),
('pityriasis-rosea','Pityriasis rosea','common','oval salmon patches with collarette scale along cleavage lines','patch','reassurance and itch relief; pregnancy requires individualized assessment','supportive care and follow-up','discharge'),
('guttate-psoriasis','Guttate psoriasis','common','numerous small drop-like scaly papules after recent sore throat','papule','skin-directed treatment and consider throat history; avoid reflexive antibiotics without indication','emollient + site-appropriate anti-inflammatory therapy','discharge'),
('squamous-cell-carcinoma-in-situ','Squamous cell carcinoma in situ','cancer','persistent sharply demarcated scaly erythematous plaque on sun-exposed skin','plaque','biopsy if uncertain; choose treatment by site, size, and patient factors','biopsy then site-appropriate definitive therapy','refer'),
('melanoma-in-situ','Melanoma in situ','cancer','irregular evolving pigmented macule with asymmetric network','macule','diagnostic biopsy and specialist-directed definitive excision','biopsy + expedited specialist referral','refer'),
]
questions=['Onset and duration','Itch versus pain','New medications','Sun exposure and tanning','Personal and family skin cancer history','Immunosuppression','Prior treatments','Occupation and hobbies','Pregnancy and contraception status','Systemic symptoms']
maneuvers=['General appearance','Focused lesion exam','Full skin exam','Mucosal exam','Nails and hair','Lymph nodes','Nikolsky sign','Wood lamp','Dermoscopy']
common_answers={
'Onset and duration':'The change began gradually over several weeks.','Itch versus pain':'There is mild itch and no disproportionate pain.','New medications':'No new medication in the past two months.','Sun exposure and tanning':'Outdoor exposure is intermittent; no tanning bed use.','Personal and family skin cancer history':'No personal skin cancer; family history reviewed.','Immunosuppression':'No known immunosuppression.','Prior treatments':'Over-the-counter moisturizer gave little relief.','Occupation and hobbies':'No clear occupational exposure identified.','Pregnancy and contraception status':'Pregnancy possibility and goals should be reviewed before teratogenic therapies.','Systemic symptoms':'No fever or systemic symptoms.'}
presentations={
'acne-vulgaris':('Breakouts and tender bumps on the face','face and upper trunk',24,'F','general'),
'atopic-dermatitis':('Recurring itchy rash in the elbow creases','flexural elbows',24,'F','general'),
'plaque-psoriasis':('Thick scaly spots on the elbows and knees','elbows and knees',37,'M','general'),
'seborrheic-dermatitis':('Flaking scalp and eyebrows','scalp and central face',46,'M','general'),
'tinea-corporis':('A ring-shaped itchy patch on the arm','forearm',29,'F','pregnant'),
'verruca-vulgaris':('A rough bump on one finger','finger',17,'F','pediatric'),
'molluscum-contagiosum':('Small bumps spreading on the arm','arm',8,'M','pediatric'),
'rosacea':('Facial flushing and small bumps','central face',32,'F','general'),
'hidradenitis-suppurativa':('Recurring painful bumps in the underarms','axillae',28,'F','general'),
'acute-urticaria':('Raised itchy welts that come and go','trunk',66,'M','geriatric'),
'allergic-contact-dermatitis':('An itchy rash where a watch touches the wrist','wrist',35,'F','general'),
'irritant-contact-dermatitis':('Burning cracked hands after frequent washing','hands',40,'M','general'),
'tinea-pedis':('Scaling and itching between the toes','interdigital feet',59,'M','general'),
'seborrheic-keratosis':('A stuck-on waxy spot on the back','back',71,'F','geriatric'),
'androgenetic-alopecia':('Gradual patterned hair thinning','scalp',52,'M','general'),
'onychomycosis':('Thickening and discoloration of a toenail','great toenail',71,'F','geriatric'),
'actinic-keratosis':('A rough spot on the sun-exposed scalp','scalp',74,'M','geriatric'),
'basal-cell-carcinoma':('A slowly enlarging spot that sometimes bleeds','cheek',63,'F','general'),
'cutaneous-squamous-cell-carcinoma':('A tender growing spot on the forearm','forearm',68,'M','immunosuppressed'),
'melanoma':('A changing dark spot on the shoulder','shoulder',44,'F','general'),
'atypical-nevus':('A mole that looks different from the others','back',31,'M','general'),
'lentigo-maligna':('A slowly enlarging brown spot on the cheek','cheek',77,'F','geriatric'),
'early-sjs-ten':('Skin pain and mouth sores with a new rash','trunk and oral mucosa',29,'F','general'),
'dress':('A new rash, facial swelling, and fever','face and trunk',42,'M','general'),
'pemphigus-vulgaris':('Painful mouth sores and fragile blisters','oral mucosa and trunk',55,'F','general'),
'bullous-pemphigoid':('Severe itching and large blisters','abdomen and limbs',82,'F','geriatric'),
'dermatomyositis':('A new rash and difficulty climbing stairs','hands, eyelids, and upper chest',48,'F','general'),
'cutaneous-lupus':('A sun-triggered scaly rash with lingering marks','cheeks and forearms',34,'F','general'),
'mycosis-fungoides':('Persistent patches on the trunk despite eczema care','trunk',61,'M','general'),
'necrotizing-infection':('Rapidly worsening severe pain and redness','lower leg',57,'M','general'),
'calciphylaxis':('Very painful dark skin lesions during dialysis','thigh',68,'F','geriatric'),
'drug-eruption':('A widespread rash after a recently started medicine','trunk',38,'M','general'),
'stasis-dermatitis':('Itchy scaly lower legs with swelling','lower legs',76,'F','geriatric'),
'scabies':('Severe nighttime itching shared by household members','finger webs and wrists',12,'F','pediatric'),
'impetigo':('Crusted sores near the nose','perinasal skin',6,'M','pediatric'),
'alopecia-areata':('A smooth round patch of hair loss','scalp',16,'F','pediatric'),
'pityriasis-rosea':('An itchy eruption that spread across the trunk','trunk',19,'F','general'),
'guttate-psoriasis':('Many small scaly spots after a sore throat','trunk',22,'M','general'),
'squamous-cell-carcinoma-in-situ':('A persistent scaly patch on the lower leg','lower leg',70,'F','geriatric'),
'melanoma-in-situ':('An irregular spot that has recently changed','upper back',51,'F','general'),
}
for idx,(cid,dx,category,clue,morph,acceptable,plan,dispo) in enumerate(cases):
    urgent=category=='urgent'
    is_cancer=category=='cancer'
    name=dx.replace('Early SJS/TEN','Early SJS/TEN').replace('DRESS','DRESS')
    age=[8,24,37,46,59,71,32,18,52,66][idx%10]
    sex=['F','M','F','M'][idx%4]
    site= ['forearm','cheek','scalp','hand','trunk','lower leg','finger','intertriginous skin'][idx%8]
    presentation=presentations.get(cid,{})
    if presentation:
        age,sex,context=presentation[2],presentation[3],presentation[4]
        site=presentation[1]
    if cid=='early-sjs-ten': age,sex,site=29,'F','trunk and oral mucosa'
    if cid=='dress': age,sex,site=42,'M','face and trunk'
    if cid=='calciphylaxis': age,sex,site=68,'F','thigh'
    ans=dict(common_answers)
    if cid=='cutaneous-squamous-cell-carcinoma': ans['Immunosuppression']='Kidney transplant recipient taking long-term immunosuppression; this changes skin cancer risk.'
    if cid=='tinea-corporis': ans['Pregnancy and contraception status']='Pregnant in the second trimester; discuss treatment with the obstetric team and prefer conservative topical care.'
    if cid=='molluscum-contagiosum': ans['Systemic symptoms']='No fever or systemic symptoms; this is a healthy school-age child.'
    if cid in ('early-sjs-ten','dress','drug-eruption'): ans['New medications']='A recently started medication is a potential culprit; reconcile exact timing and notify the prescribing team.'
    if cid=='mycosis-fungoides': ans['Prior treatments']='Several topical steroid courses gave transient improvement; lesions return in the same areas.'
    if cid=='calciphylaxis': ans['Immunosuppression']='End-stage kidney disease on hemodialysis; review mineral-bone parameters and vascular risk.'
    ans['Focused clue']=clue
    ans['Onset and duration']= ('A new eruption began 9 days after starting a medication.' if cid in ('early-sjs-ten','dress','drug-eruption') else ('Progression has been rapid over 36 hours.' if cid=='necrotizing-infection' else common_answers['Onset and duration']))
    ans['Itch versus pain']=('Deep skin pain is severe and out of proportion to visible findings.' if cid in ('early-sjs-ten','necrotizing-infection','calciphylaxis') else common_answers['Itch versus pain'])
    ans['New medications']=('A recently started medication is a potential culprit; reconcile exact timing.' if cid in ('early-sjs-ten','dress','drug-eruption') else common_answers['New medications'])
    ans['Systemic symptoms']=('Fever and malaise are present; this is an emergency.' if cid in ('early-sjs-ten','dress','necrotizing-infection') else common_answers['Systemic symptoms'])
    exam={m:'No additional abnormality found on this maneuver.' for m in maneuvers}
    exam['Focused lesion exam']=clue.capitalize()+'.'
    exam['General appearance']='Alert and conversant; vital signs must be checked in real practice.'
    if cid in ('early-sjs-ten','pemphigus-vulgaris'): exam['Mucosal exam']='Painful oral erosions are present.'
    if cid=='early-sjs-ten': exam['Nikolsky sign']='Tender dusky plaques with early epidermal fragility; urgent escalation indicated.'
    if cid=='pemphigus-vulgaris': exam['Nikolsky sign']='Positive at lesion edge.'
    if cid=='bullous-pemphigoid': exam['Nikolsky sign']='Negative; tense bullae on urticarial plaques.'
    if cid=='melanoma': exam['Dermoscopy']='Asymmetric network and irregular dots/globules; concerning evolution.'
    if is_cancer: exam['Lymph nodes']='No palpable regional lymphadenopathy; assess by site and risk.'
    if cid=='dermatomyositis': exam['General appearance']='Subtle heliotrope discoloration; ask about proximal weakness and swallowing.'
    if cid=='calciphylaxis': exam['Focused lesion exam']='Retiform purpura with necrotic center and extreme tenderness.'
    case={
      'id':cid,'category':category,'demographics':{'age':age,'sex':sex,'pregnancyRelevant':sex=='F' and age<50,'context': context if presentation else ('pediatric' if age<18 else ('geriatric' if age>=65 else 'general'))},
      'chiefComplaint':(presentation[0] if presentation else f"{('Painful' if cid in ('necrotizing-infection','calciphylaxis') else 'Changing')} skin finding on the {site}"),'lesionSite':site,'hiddenDiagnosis':dx,'urgency':('critical' if urgent else ('high' if is_cancer else 'routine')),
      'historyAnswers':ans,'examFindings':exam,'image':{'file':f'{cid}.svg','status':'needs_image','alt':f'Original vector placeholder, not a clinical photograph: generic abstract lesion swatch at the {site}; no diagnosis or patient is depicted.'},'imageStatus':'needs_image',
      'correctMorphology':[morph.title(), 'Scale' if 'scale' in clue else morph.title()], 'acceptableDifferential':[dx]+(['melanoma','pigmented nevus'] if is_cancer else ['eczema','contact dermatitis']),
      'tests':[{'name':'Dermoscopy','result':exam.get('Dermoscopy','No diagnostic dermoscopy clue in this case.'),'minutes':4,'indicated':is_cancer}, {'name':'Punch biopsy with H&E','result':'Histopathology supports the hidden diagnosis when properly sampled.','minutes':18,'indicated':is_cancer or urgent}, {'name':'KOH prep','result':'No fungal elements seen.','minutes':8,'indicated':cid in ('tinea-corporis','tinea-pedis')}, {'name':'CBC and CMP','result':'Results should be interpreted with clinical context.','minutes':12,'indicated':cid in ('dress','dermatomyositis','calciphylaxis')}, {'name':'Photo documentation','result':'Baseline clinical photograph recorded with consent.','minutes':3,'indicated':True}],
      'acceptableTreatments':[{'name':plan,'reason':acceptable}],
      'unacceptableTreatments':[{'name':'High-potency topical corticosteroid on face or folds','reason':'Site-related atrophy risk; choose site-appropriate treatment.'},{'name':'Systemic corticosteroid for an undifferentiated rash','reason':'May obscure diagnosis and worsen some infections.'},{'name':'Methotrexate without baseline assessment','reason':'Requires screening, labs, pregnancy precautions, and specialist oversight.'},{'name':'Biologic therapy without infection screening','reason':'Requires appropriate screening and specialist plan.'},{'name':'Spironolactone without pregnancy and contraindication review','reason':'Review pregnancy goals, relevant contraindications, and monitoring before use.'},{'name':'Isotretinoin without pregnancy prevention steps when applicable','reason':'Major teratogenic risk; follow current prescribing safeguards.'}],
      'idealDisposition':dispo,'teachingPearl':acceptable+' Reassess if the course changes or red flags emerge.','traps':['Anchoring on morphology without asking about timing','Using a potent topical steroid on thin or intertriginous skin','Missing medication timing or mucosal symptoms','Ordering biopsy without a decision-changing question'],'needsReview':True,'urgentReason':('Time-sensitive pattern; emergency escalation takes priority over office testing.' if urgent else None)
    }
    Path('src/data/cases',f'{cid}.json').write_text(json.dumps(case,indent=2)+'\n')
Path('src/data/cases/index.json').write_text(json.dumps([x[0] for x in cases],indent=2)+'\n')
print(f'Wrote {len(cases)} cases')
