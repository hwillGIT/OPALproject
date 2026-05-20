# LYNA UI Implementation

This directory contains implementation files and HTML prototypes for
LYNA's interfaces — v1 iPhone app, manager dashboard, and (deferred)
v3 dedicated badge.

## Quick start — open the prototype

```
implementation/html-mockups/index.html
```

Opens a browser landing page indexing every available mock. Use this
as the entry point for design reviews and stakeholder demos.

## Structure

```
implementation/
├── html-mockups/
│   ├── index.html              ← START HERE — landing page
│   ├── v1/                     ← v1 iPhone-app mocks (canonical)
│   │   ├── lyna.css
│   │   ├── s1a-home.html
│   │   ├── s3b-ai-pill.html
│   │   ├── s4a-brain-sheet.html
│   │   ├── s5a-critical-alert.html
│   │   ├── s6a-broadcast.html
│   │   └── s7b-interpreter.html
│   ├── dashboard-v1/           ← Manager dashboard mocks (canonical)
│   │   ├── lyna-dashboard.css
│   │   ├── d1-adoption.html
│   │   ├── d2-ai-tools.html
│   │   └── d10-roi.html
│   ├── device-home.html        ← v3 reference (pre-I-Corps)
│   └── dashboard-overview.html ← v3 reference (pre-I-Corps)
├── html-prototype/
│   └── device-prototype.html   ← v3 reference (pre-I-Corps)
├── lvgl-theme/                 ← v3-specific embedded theme
├── react-dashboard/            ← React skeleton for the manager dashboard
└── README.md
```

## v1 iPhone mocks (current canonical — complete set)

Each HTML file renders one surface inside an iPhone 14 frame
(390 × 844pt, with status bar + dynamic island + home indicator).
Shared CSS in `v1/lyna.css` carries the LYNA design tokens (mode
colors blue/orange/purple, typography, spacing, motion).

| File | Surface | Journey |
|---|---|---|
| `v1/s1a-home.html` | S1.A Home / mode indicator | All journeys (entry point) |
| `v1/s1bcd-voice-states.html` | S1.B/C/D/E Voice command states | All journeys |
| `v1/s2a-mode-switcher.html` | S2.A Mode switcher modal | §4.8, §4.10 entry |
| `v1/s3a-response-card.html` | S3.A Standard response card | §4.1 Sarah (pain med) |
| `v1/s3b-ai-pill.html` | S3.B Response Card with hospital AI pill | §4.6 Robert (AI routing) |
| `v1/s3c-first-time-ai.html` | S3.C First-time AI exposure card | §4.6 Robert |
| `v1/s4a-brain-sheet.html` | S4.A Unit brain sheet | §4.3 Marcus (charge handoff) |
| `v1/s4b-signon.html` | S4.B Assignment brain sheet | §4.4 Jamal (sign-on) |
| `v1/s5a-critical-alert.html` | S5.A Critical Alert full-screen | §4.7 Sofia (rapid response) |
| `v1/s5bc-alert-followup.html` | S5.B Status banner + S5.C Protocol view | §4.7 follow-up |
| `v1/s6a-broadcast.html` | S6a Broadcast sender ack tracker | §4.8 Priya (isolation) |
| `v1/s6b-broadcast-receiver.html` | S6b Receiver banner | §4.8 receivers |
| `v1/s7a-interpreter-compliance.html` | S7.A Compliance modal | §4.10 Maya entry |
| `v1/s7b-interpreter.html` | S7.B Active interpreter session | §4.10 Maya |
| `v1/s8-camera-handoff.html` | S8 Camera handoff (both states) | §4.9 Aisha (pressure injury) |
| `v1/s9-login.html` | S9 Login / shift start (3 steps) | All journeys (once per shift) |
| `v1/s10-settings.html` | S10 Settings | (rare) |

## Dashboard mocks (current canonical — complete set)

| File | View | Primary user |
|---|---|---|
| `dashboard-v1/d1-adoption.html` | D1 Adoption overview | Unit manager (H13) |
| `dashboard-v1/d2-ai-tools.html` | D2 AI tool routing | CCIO (H6, H17, H18) |
| `dashboard-v1/d3-top-queries.html` | D3 Top queries (answered + unanswered) | NI team |
| `dashboard-v1/d4-response-times.html` | D4 Response times | CCIO (efficiency, H2) |
| `dashboard-v1/d5-abandonment.html` | D5 Silent abandonment alerts | Unit manager (H13) |
| `dashboard-v1/d6-broadcast-coverage.html` | D6 Broadcast / help coverage | Unit manager, quality |
| `dashboard-v1/d7-critical-audit.html` | D7 Critical alerts audit | Quality / safety |
| `dashboard-v1/d8-interpreter-sessions.html` | D8 Interpreter sessions | NI team, language services |
| `dashboard-v1/d9-per-tool.html` | D9 Per-AI-tool detail (drill from D2) | CCIO (renewal conversations) |
| `dashboard-v1/d10-roi.html` | D10 Buyer-facing ROI | CCIO / CNO / CFO (H10) |

## v3 reference (deferred design pass)

The pre-I-Corps OPAL-device assets are kept as v3 reference:

- `html-mockups/device-home.html` — dedicated-device home screen
- `html-mockups/dashboard-overview.html` — earlier dashboard concept
- `html-prototype/device-prototype.html` — interactive device prototype
- `lvgl-theme/` — embedded LVGL theme for the device

See `../v3-design-alignment.md` for the v3 work plan once v1 pilot
data lands.

## Design Tokens

`../design-tokens.json` is the source of truth for colors, typography,
spacing. Both `v1/lyna.css` and `dashboard-v1/lyna-dashboard.css`
mirror these tokens. The LVGL theme uses the same tokens.

## React dashboard

`react-dashboard/` is the implementation starting point for the
manager dashboard. Follow its README for setup. The HTML mocks in
`dashboard-v1/` are the visual reference for what to build.

## Next steps

1. **Open `html-mockups/index.html`** in a browser to review the
   first-pass prototype.
2. **Iterate on tone / detail** with stakeholders before completing
   the remaining surfaces and views.
3. **Use Claude Design** (claude.ai/design) for variations or
   alternative explorations — see `../claude-design-briefs.md` for
   paste-ready prompts.
4. **Wire up the React dashboard** to back D1/D2/D10 with real data
   from the memory event log.
5. **Defer v3** until v1 pilot data is in.

## Resources

- [LYNA design system](../opal-design-system.md)
- [Design tokens](../design-tokens.json)
- [v1 UX spec](../opal-interaction-flows.md)
- [v1 wireframes](../opal-ui-wireframes-v1.md)
- [v1 screen designs](../opal-screen-designs-v1.md)
- [Dashboard spec](../manager-dashboard.md)
- [Dashboard wireframes](../manager-dashboard-wireframes.md)
- [Dashboard screen designs](../manager-dashboard-screen-designs.md)
- [Claude Design briefs](../claude-design-briefs.md)
- [v3 alignment](../v3-design-alignment.md)
