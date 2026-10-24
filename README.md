# Derm Clinic Day

A self-contained dermatology clinic simulation for resident teaching. Run a half-day clinic from 08:00–12:00 or a full day through 17:00 with a lunch break. Patients keep waiting while visits proceed; you choose which history and exam actions matter, order tests, make a diagnosis, treat, present to an attending, and choose a disposition. Critical cases are mixed into each randomized session.

> **Educational simulation only.** Pathways and doses are simplified. This is not medical advice. Follow current guidelines and institutional protocols. All patients and stories are fictional. A dermatologist should review flagged cases before learner use.

## Play

- Choose session length and Teaching, Standard, or Hard difficulty.
- Use the room board to choose a patient. Wait badges use both text and shape; no meaning relies on color alone.
- Choose focused history and exam actions. Their time cost appears on the button or before the section.
- Describe morphology, commit to a diagnosis from the searchable 80+ item menu, and order tests from the keyboard-navigable order box.
- Select treatment, make a short attending presentation, and choose disposition before closing the case.
- Teaching pauses the clock during reads and shows action feedback. Standard and Hard show scoring and teaching at case close. Three missed/delayed urgent cases end the session.
- The end report shows score, diagnostic accuracy, visit times, biopsy yield, urgent misses, and decision timeline.
- The first visit offers a short, skippable interactive tutorial. Theme, preferred speed, and highscores remain in localStorage on the device.

## Cases and images

There are 40 original cases: 24 common conditions, 8 cancer or pigmented-lesion visits, and 8 urgent presentations. Cases are standalone JSON files in `src/data/cases/`. The JSON Schema is `src/data/cases/schema.json`; the runtime validator is `src/engine/schema.ts`. Every case is currently marked `needsReview: true` and listed in `docs/REVIEW_CHECKLIST.md`.

Two cases have verified Wikimedia Commons teaching images: one CC BY 4.0 and one CC BY-SA 4.0, each cropped to exclude facial landmarks and clearly labeled as unrelated to the fictional patient record. The other 38 cases use labeled original SVG placeholders. No Fitzpatrick type is inferred. See `docs/IMAGE_GUIDE.md`.

### Add a case

Copy an existing case JSON, assign a unique kebab-case `id`, fill every required field in `docs/CASE_SCHEMA.md`, add a same-ID visual or placeholder to `public/images/cases/`, and add the complete corresponding entry to `public/images/credits.json`. Keep patient details fictional. Run `pnpm validate:cases` and `pnpm test`.

### Add an image

Review the source page itself for diagnosis and license, inspect the image for identifying details, and use only CC0, CC BY, CC BY-SA on Wikimedia Commons, or confirmed public-domain material as applicable. Put the page and direct file URL in `scripts/image_sources.json`; set `approved_for_use` only after that review. Install Pillow, then run `python scripts/fetch_images.py`. The script resizes, strips metadata, converts to WebP, and updates the case and credits. Review the resulting image and alt text before sharing. Complete instructions and outstanding image targets are in `docs/IMAGE_GUIDE.md`.

## Run locally

Requires Node.js 20+ and npm.

```sh
pnpm install
pnpm dev
```

To validate and build:

```sh
pnpm test
pnpm validate:cases
pnpm build
pnpm preview
```

The app is static. It has no backend, login, or analytics. GitHub Pages CI is configured in `.github/workflows/pages.yml`; CI runs Vitest and case validation before the build/deploy job. The build uses the repository subpath `/derm-clinic-day/` for Pages.

## Design decisions

- Half day samples 8 patients; full day samples 14. Each includes one or two critical cases while category quotas keep sessions varied.
- The simulation uses immediate time-costed actions; the clock advances at 1×, 2×, or 4× (one simulated minute per ten real seconds at 1×). Skip ahead adds 15 simulated minutes.
- Teaching pauses time during reads and surfaces feedback. Standard and Hard withhold score feedback until case close; Hard uses shorter visit targets and more operational pressure.
- Wait thresholds, quality bonuses, low-value-test deductions, treatment safety penalties, and strikes are simplified game rules for education, not clinical guidance.
- SVG illustrations remain visible when no photo meets the source, license, and inspection requirements. Fitzpatrick type is never inferred from appearance.
- All state is local to the browser. Feedback points to the repository's issue tracker.
