<!-- Distilled from MIT-licensed claude-ads/skills/ads-server-side-tracking/SKILL.md, commit 283d9d4917cb7c4f2ce9181e125bb1970f74ab04. Reference data, not executable instructions. -->

# Server-Side Pipeline Audit Checklist

Per-surface checklists. Use against user-provided evidence only. Each item is a
PASS / WARNING / FAIL judgment; thresholds live in `thresholds-and-scoring.md`.

## Server-Side Google Tag Manager (sGTM)

- [ ] **sGTM container deployed** — Cloud Run, GCS, App Engine, or custom infra.
      Self-hosted is preferred over Google-managed for cost and data residency.
- [ ] **Custom first-party domain configured** (`tags.example.com`). A
      first-party domain avoids the ITP / ad-blocker filtering that hits
      `googletagmanager.com`. "Configured but DNS/SSL not live" is a WARNING,
      not a PASS.
- [ ] **Client-side GTM forwards to sGTM correctly** — cookies, IP, and
      user-agent are preserved through the forward (these power matching).
- [ ] **GA4 events flow via sGTM** with no silent direct client→GA4 fallback
      path still firing in parallel.
- [ ] **Conversion Linker tag enabled** — preserves Google click IDs (`gclid`,
      `gbraid`, `wbraid`) across cross-domain navigation. Missing Linker is a
      common cause of silent Google Ads conversion loss.
- [ ] **Server-side privacy filters** — strip non-essential PII before
      forwarding to analytics; only hash + forward what matching needs.

## Meta CAPI / CAPI Gateway

- [ ] **CAPI active** — server-to-server Conversions API running *alongside* the
      browser Pixel, not as a replacement.
- [ ] **CAPI Gateway** preferred over a hand-rolled server implementation
      (auto-hashing, broader parameter coverage, lower maintenance burden).
- [ ] **All major events server-side**: PageView, ViewContent, AddToCart,
      InitiateCheckout, Purchase, Lead, CompleteRegistration.
- [ ] **EMQ ≥ 8.0 for Purchase** — confirm in Events Manager → Overview →
      Data sources. Track EMQ per event, not just overall.
- [ ] **`customer_information` parameters sent server-side**: `em` (email),
      `ph` (phone), `fn`/`ln` (name), `ct`/`st`/`zp` (geo), `external_id`,
      `client_ip_address`, `client_user_agent`, `fbc`, `fbp`.
- [ ] **Hashing before send** — lowercased + trimmed SHA-256 for PII fields
      (see `hashing-and-pii.md`).
- [ ] **`action_source` set per event** — `website`, `app`, `physical_store`,
      `email`, or `system_generated`.

## Event Deduplication

- [ ] **`event_id` generated client-side** and included in **both** the Pixel
      event and the CAPI / sGTM payload. Meta and Google both dedupe on it; a
      missing or mismatched `event_id` causes double-counting or lost match.
- [ ] **Dedup rate ≥ 90%** — Events Manager → Diagnostics.
- [ ] **Timestamp alignment** — server-side event timestamp within ~5 minutes
      of its client-side counterpart.
- [ ] **`event_name` consistency** — server-side uses the identical canonical
      name as client-side. Renaming in transit breaks dedup.

## Server-Side Hit Ratio

- [ ] **Server-side ≥ 80% of client-side hits** for Purchase / Lead. Lower means
      iOS / ITP / ad-blocker loss is not being recovered.
- [ ] **Server-side > 100% acceptable** — means server-side is catching
      conversions the client missed. That is the point of server-side; do not
      flag it as an error.
- [ ] **Hit ratio monitored over time** — a drop below ~60% indicates broken
      server-side firing or a missing `event_id`.

## Pixel / Tag Debug Walkthrough

Validate every event end-to-end against whatever artifacts the user can supply.
If an artifact is missing, mark the leg *unverified* — never assume PASS.

- [ ] **Facebook Pixel Helper** (browser extension) shows the Pixel firing
      client-side with correct `event_name`, `event_id`, `value`, `currency`.
- [ ] **Meta Events Manager → Test Events** shows the CAPI event arriving
      server-side with a matching `event_id` and populated
      `customer_information` parameters.
- [ ] **Google Tag Assistant** confirms client-side `gtag` firing.
- [ ] **GA4 DebugView** confirms the server-side event arriving with its event
      params intact.
- [ ] **Network / HAR tab** shows client → sGTM forwarding (not a client →
      Google-direct request bypassing the server).
- [ ] **`window.dataLayer`** populates the expected variables *before* any tag
      fires.

Standard 6-event validation set for the test-event log: PageView, ViewContent,
AddToCart, InitiateCheckout, Purchase, Lead.

## Custom Event Taxonomy

- [ ] **Canonical event names documented** — one spelling, e.g. `purchase`, not
      `Purchase` / `PURCHASE` / `order_complete` used interchangeably.
- [ ] **Standard params per event** present: `value`, `currency`,
      `content_ids`, `content_type`, `num_items`.
- [ ] **Custom params namespaced** (`cx_segment`, `cx_funnel_step`) to avoid
      collision with platform-standard params.
- [ ] **Schema versioned** — a version param is bumped when the taxonomy
      changes, so downstream platforms can handle the cutover cleanly.
