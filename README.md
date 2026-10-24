# Derm Clinic Day

A self-contained dermatology clinic simulation for resident teaching. Run a half-day clinic from 08:00–12:00 or a full day through 17:00 with a lunch break. Patients keep waiting while visits proceed; you choose which history and exam actions matter, order tests, make a diagnosis, treat, present to an attending, and choose a disposition. Critical cases are mixed into each randomized session.

> **Educational simulation only.** Pathways and doses are simplified. This is not medical advice. Follow current guidelines and institutional protocols. All patient stories are fictional. A dermatologist should review flagged cases before learner use.

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

The playable library contains 28 fictional cases, each paired with a photograph supplied for this game. `src/data/cases/index.json` lists the active case IDs; cases not in that index are not loaded. Case JSON files are in `src/data/cases/`, with the JSON Schema at `src/data/cases/schema.json` and runtime validation in `src/engine/schema.ts`. Every active case remains marked `needsReview: true`.

The photos are independent teaching images and do not depict the fictional case records. The user confirmed permission to use the supplied images; source URLs, photographer names, and public-license details were not provided. Image credits state this explicitly, and no Fitzpatrick type is inferred. See `docs/IMAGE_GUIDE.md`.

### Add a case

Copy an existing case JSON, assign a unique kebab-case `id`, fill every required field in `docs/CASE_SCHEMA.md`, add its image to `public/images/cases/`, add an attribution record to `public/images/credits.json`, and include the ID in `src/data/cases/index.json` only when the case has a supplied, permitted photograph. Keep patient details fictional.

### Add an image

Inspect the supplied image and confirm permission before use. Record the source, author, and license only when those details are available; never infer or invent them. Use descriptive alt text that matches visible findings, avoid personal identifiers, and state when the photo is separate from the fictional patient record.

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
- All state is local to the browser. Feedback points to the repository's issue tracker.
