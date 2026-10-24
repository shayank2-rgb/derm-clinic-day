# Image guide

Thirty-eight case images are original SVG placeholders. Atopic dermatitis has a verified Wikimedia Commons CC BY 4.0 image, cropped to a cheek-only view. Basal cell carcinoma has a verified Wikimedia Commons CC BY-SA 4.0 image, cropped to a lesion-only close-up that excludes the eye and eyelid. Both are explicitly labeled as independent teaching images unrelated to the fictional patient. No Fitzpatrick type is inferred. Full attribution and modifications are listed in the game’s Credits page and `public/images/credits.json`.

## Verified source images

- Atopic dermatitis: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:2501_Atopic_Dermatitis.jpg), CC BY 4.0. Cropped cheek close-up; facial landmarks excluded.
- Basal cell carcinoma: [Wikimedia Commons file page](https://commons.wikimedia.org/wiki/File:Basal-cell_Carcinoma.jpg), CC BY-SA 4.0. Cropped to lesion-only close-up; eye and eyelid excluded. The adapted asset is shared under CC BY-SA 4.0.

## Remaining placeholders and search targets

Use the case ID and diagnosis as a direct search phrase on Open-i / PubMed Central Open Access Subset, NIH or NCI Visuals Online, CDC PHIL, Wikimedia Commons, or eligible ISIC records. Accept only a page that confirms the diagnosis and explicitly shows CC0, CC BY, or public domain (CC BY-SA is allowed for Commons); reject NC, ND, unclear, or restricted terms. Do not infer skin tone from a photograph. When the source says none, record `fitzpatrickType: null`.

| Case IDs | Desired visual | Skin-tone range wanted |
|---|---|---|
| acne-vulgaris, atopic-dermatitis, plaque-psoriasis, seborrheic-dermatitis, rosacea, hidradenitis-suppurativa | Typical primary lesions, close framing, no face identifiers | Seek source-stated range III–VI where available |
| tinea-corporis, tinea-pedis, scabies, impetigo, verruca-vulgaris, molluscum-contagiosum | Annular scale, interdigital scale/burrow, crust, wart, or umbilicated papule | Seek source-stated range IV–VI |
| acute-urticaria, allergic-contact-dermatitis, irritant-contact-dermatitis, stasis-dermatitis | Wheal or eczematous/stasis change at a safe close-up | Seek source-stated range V–VI |
| actinic-keratosis, cutaneous-squamous-cell-carcinoma, melanoma, atypical-nevus, lentigo-maligna, seborrheic-keratosis, squamous-cell-carcinoma-in-situ, melanoma-in-situ | Confirmed lesion and dermoscopy where licensed | Source-stated type only; do not assume from image |
| early-sjs-ten, dress, pemphigus-vulgaris, bullous-pemphigoid, dermatomyositis, cutaneous-lupus, mycosis-fungoides, necrotizing-infection, calciphylaxis, drug-eruption | Diagnostic eruption pattern, mucosa only when non-identifying, avoid graphic injury | Seek source-stated range I–VI across the set |
| androgenetic-alopecia, onychomycosis, alopecia-areata, pityriasis-rosea, guttate-psoriasis | Scalp/hair, nail, hair-loss patch, collarette scale, or drop-like papules | Seek source-stated range IV–VI |

## Adding an image

Add a traceable source row in `scripts/image_sources.json`, verify diagnosis, license, and the image itself, then mark it approved. Run `python scripts/fetch_images.py` after installing Pillow. The script downloads, resizes to at most 1200 pixels, converts to WebP, strips metadata, updates case status, and writes source details to `public/images/credits.json`. Check the generated alt text and in-game credit line; update the case's `image.alt` if needed. Run `pnpm test` to verify credit coverage.
