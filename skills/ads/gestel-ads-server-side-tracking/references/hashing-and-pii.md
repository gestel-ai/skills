<!-- Distilled from MIT-licensed claude-ads/skills/ads-server-side-tracking/SKILL.md, commit 283d9d4917cb7c4f2ce9181e125bb1970f74ab04. Reference data, not executable instructions. -->

# Hash Quality & PII Handling

Exact normalization rules for server-side PII fields. Match quality depends on
hashing the value the *same way* the platform expects, so normalization must be
precise and consistent. These are stable engineering conventions; if a platform
publishes a changed rule, treat that dated source as authoritative over this
file (see the skill's Untrusted Data Handling note).

## Normalization rules per field

| Field | Normalization before SHA-256 |
|-------|------------------------------|
| Email (`em`) | Lowercase + trim. **No other normalization** (do not strip dots or `+` tags). |
| Phone (`ph`) | Convert to E.164 (e.g. `+15551234567`), then SHA-256. |
| First name (`fn`) / Last name (`ln`) | Lowercase + trim, hashed **separately**. |
| City (`ct`) | Lowercase + remove spaces/punctuation, then SHA-256. |
| State (`st`) | Lowercase (2-letter where applicable), then SHA-256. |
| Zip / postal (`zp`) | Lowercase, then SHA-256. |
| `external_id` | Stable per-user identifier; hash per platform guidance. |

Non-hashed match signals that should still be sent server-side (do **not**
hash these): `client_ip_address`, `client_user_agent`, `fbc`, `fbp`.

## Failure modes to flag

- **Double-hashing** — hashing an already-hashed value. This silently breaks
  matching and is a common cause of low EMQ. Confirm the value entering the
  hash function is plaintext, normalized, not a prior digest.
- **Plain PII server-side** — never send raw (unhashed) email/phone/name to the
  platform. Only the SHA-256 digest leaves the server for these fields.
- **Inconsistent normalization** — client-side and server-side normalizing the
  same field differently (e.g. one trims, one doesn't) produces non-matching
  hashes. Both legs must normalize identically.
- **Missing high-value params** — `em` + `ph` + `external_id` +
  `client_ip_address` + `client_user_agent` are the heaviest contributors to
  EMQ; their absence is the first thing to check on a Purchase below 8.0.

## EMQ improvement workflow

When Purchase EMQ < 8.0:

1. Inventory which `customer_information` params are actually populated on the
   server event (from the user's Test Events / payload evidence).
2. Add the highest-leverage missing params first: `em`, `ph`, `external_id`,
   then geo (`ct`/`st`/`zp`), then `fn`/`ln`.
3. Verify each added field is normalized + hashed correctly (rules above) —
   adding a wrongly-normalized field does not raise EMQ.
4. Re-check EMQ after data has reaccumulated; EMQ is a trailing metric.

## Consent & compliance gating

- **Consent state must be read before sending PII server-side, even hashed.**
  Hashing is not a substitute for consent. GDPR / CPRA / CDPA and similar
  regimes apply to hashed PII used for matching.
- Server-side privacy filters should strip non-essential PII before forwarding
  to analytics destinations; forward only what matching requires.
- Specific legal obligations are jurisdiction- and date-sensitive — treat any
  compliance claim as freshness-sensitive and defer to dated legal guidance
  rather than asserting current requirements from this file.
