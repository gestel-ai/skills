<!-- Updated: 2026-06-28 | v1.0 -->
<!-- Used by: gestel-seo-bing -->
<!-- FRESHNESS: Endpoints, participating-engine roster, and key-length bounds are
     dated snapshots from the source's 2024-2025 window. Confirm with a live
     lookup before asserting as current. The methodology below is stable. -->

# IndexNow protocol — setup, verification, submission, troubleshooting

IndexNow is an **open protocol** for telling participating search engines that a
URL was created, updated, or deleted, so they can crawl it promptly. The only
"credential" is a key the **site owner generates and publishes on their own
domain** — there is no paid provider and no third-party account. Google does
**not** participate (it publicly rejects IndexNow); this is a Bing / Yandex /
Seznam / Naver mechanism.

## One ping, four engines

Submitting to any participating engine's endpoint shares the notification with
the others. You do **not** need to POST four times. Bing's endpoint
(`https://www.bing.com/indexnow`) is the common choice; the generic
`https://api.indexnow.org/indexnow` also works.

## Setup checklist (user performs these)

1. **Generate a key.** A hex string, 8–128 characters. Example:
   `openssl rand -hex 32` → a 64-char key.
2. **Publish the key file.** Create a UTF-8 plaintext file whose **body is
   exactly the key**, named `<key>.txt`, at the **root** of the host:
   `https://example.com/<key>.txt`. (A non-root keyLocation is allowed if you
   declare `keyLocation`, but root is simplest and least error-prone.)
3. **Confirm the file resolves.** Fetching the keyLocation URL must return HTTP
   200 with the body byte-matching the key — no surrounding whitespace, no HTML
   wrapper, no redirect to a login.

## Verification first — the #1 failure mode

Before any submission, verify the key is actually live and matches:

- Fetch `https://example.com/<key>.txt`.
- Confirm status 200 (not 404, not 301→somewhere else, not a soft-404 page).
- Confirm the response body, trimmed, equals the key exactly.

If verification fails, **stop** — submissions will be silently rejected and the
user will think IndexNow "doesn't work." Most onboarding failures are a 404 key
file, a key/keyLocation mismatch, or the file served as `text/html` with markup.

## Submission

### Single URL (GET)

```text
https://www.bing.com/indexnow?url=https%3A%2F%2Fexample.com%2Fnew-page&key=<key>
```

The `url` value must be URL-encoded. The key may also be passed via a
`keyLocation` if it is not at the root.

### Batch URLs (POST JSON)

```text
POST https://www.bing.com/indexnow
Content-Type: application/json

{
  "host": "example.com",
  "key": "<key>",
  "keyLocation": "https://example.com/<key>.txt",
  "urlList": [
    "https://example.com/page-a",
    "https://example.com/page-b",
    "https://example.com/page-c"
  ]
}
```

Rules:

- **Every URL in `urlList` must belong to the declared `host`.** Mixed-host
  payloads are rejected — split by host into separate POSTs.
- `keyLocation` is optional when the key file is at the root and named
  `<key>.txt`; include it when the key lives elsewhere.
- Keep batches reasonable (the protocol allows up to 10,000 URLs per request;
  practically, submit only URLs that actually changed).

### Response codes (typical)

| Code | Meaning | Action |
|---|---|---|
| 200 | Received | Submitted successfully (not a crawl/index guarantee) |
| 202 | Accepted, key validation pending | Ensure keyLocation is live |
| 400 | Bad request | Malformed JSON / missing field — fix payload |
| 403 | Key not valid | keyLocation 404s or body mismatch — re-verify |
| 422 | URLs don't match host / key | Split by host; check key |
| 429 | Too many requests | Back off; you're over-pinging |

## Etiquette and quota

- **Submit on change, not on a schedule.** Ping when a URL is published, updated
  meaningfully, or removed — not the whole sitemap on a cron. Re-pinging
  unchanged URLs wastes quota and can earn a 429.
- **Don't spam edits.** Trivial changes don't warrant a re-ping.
- **200 ≠ indexed.** A successful submission means *discovered/notified*, not
  *indexed* or *ranked*. The engine still applies its own quality and crawl
  decisions.

## When to reach for IndexNow

- New content launch where Copilot/Bing citation eligibility matters quickly.
- Site migration / bulk URL changes (submit the new URLs; the change is the
  point).
- Time-sensitive pages (event, release, pricing) that must be current in Bing.
- After fixing a page that was previously `noindex`/blocked and is now intended
  to be indexed.

## Boundary reminder

This document specifies **what to publish, what to send, and how to verify**. The
actual key generation, file publishing, and the live submission POST/GET are
performed by the **user or an adapter** — this skill does not hold the host key,
does not write to the user's server, and does not itself fire the request. The
upstream `indexnow_submit.py` runner referenced by the original extension is
**not present**; treat any "just run the script" assumption as a Boundary, and
hand the user a ready-to-run command instead.
