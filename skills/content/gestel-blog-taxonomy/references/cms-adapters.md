<!-- Provenance: distilled from references/skills/claude-blog/skills/blog-taxonomy/SKILL.md (claude-blog, commit 49842ea9e7b9a1f6f8a3774a3fcfb082ab6a7d25, MIT). Reference knowledge only — this skill does not execute sync. -->

# CMS Taxonomy Adapter Reference

This file documents the API surface each major CMS exposes for tags/categories.
It is **planning reference knowledge**, not an executable adapter. Pushing
taxonomy to a live CMS requires credentials, network writes, and a tested adapter,
which this skill does not provide. When a user wants an actual sync, hand this
reference to an implementation/adapter task that owns the credentials and HTTP
client (see the Boundary in `SKILL.md`).

## Adapter Overview

| CMS | API Type | Auth Method | Tags Model |
|-----|----------|-------------|------------|
| WordPress | REST | Application Passwords (base64) | First-class entities with IDs |
| Shopify | GraphQL (Admin API) | Admin API access token | String array on Article |
| Ghost | REST (Admin API) | API key with JWT signing | First-class entities |
| Strapi | REST or GraphQL | API token (Bearer) | User-defined content type |
| Sanity | GROQ / Mutations | Project token (Bearer) | Document type |

Credentials are conventionally supplied as environment variables to the adapter
that performs the write (`CMS_TYPE`, `CMS_URL`, `CMS_API_KEY`). They must never be
stored in files or committed. This skill itself reads none of these — it only
describes the contract an adapter must satisfy.

## WordPress (REST)

- List tags: `GET {CMS_URL}/wp-json/wp/v2/tags?per_page=100&search={keyword}` with header `Authorization: Basic {base64(username:app_password)}`
- Create tag: `POST {CMS_URL}/wp-json/wp/v2/tags` body `{"name": "...", "slug": "...", "description": "..."}`
- List categories (hierarchical, supports `parent`): `GET {CMS_URL}/wp-json/wp/v2/categories?per_page=100`
- Create category: `POST {CMS_URL}/wp-json/wp/v2/categories` body `{"name": "...", "slug": "...", "parent": 0}`
- Assign to post: `POST {CMS_URL}/wp-json/wp/v2/posts/{id}` body `{"tags": [1,2,3], "categories": [4]}`
- Pagination: follow the `X-WP-TotalPages` response header for full listings.

## Shopify (GraphQL Admin API)

Tags are a string array on the Article object, not first-class entities.
Auth header: `X-Shopify-Access-Token: {token}`.

Update article tags:

```graphql
mutation {
  articleUpdate(id: "gid://shopify/Article/123", article: {
    tags: ["tag-one", "tag-two", "tag-three"]
  }) {
    article { id tags }
    userErrors { field message }
  }
}
```

List all tags in use:

```graphql
{ articles(first: 250) { edges { node { id title tags } } } }
```

Note: REST API was marked legacy Oct 2024; GraphQL is required for new apps since
Apr 2025. Treat these dates as freshness-sensitive — verify before relying on them.

## Ghost (Admin API)

- List tags: `GET {CMS_URL}/ghost/api/admin/tags/?limit=all` with header `Authorization: Ghost {jwt_token}`
- Create tag: `POST {CMS_URL}/ghost/api/admin/tags/` body `{"tags": [{"name": "...", "slug": "..."}]}`
- JWT: sign with admin API key (`id:secret`), `iat = now`, `exp = now + 5min`, audience `/admin/`.

## Strapi (REST or GraphQL)

Endpoints are auto-generated from content types. Field names vary by schema.

```text
GET  {CMS_URL}/api/tags?pagination[pageSize]=100
POST {CMS_URL}/api/tags    body {"data": {"name": "...", "slug": "..."}}
Authorization: Bearer {api_token}
```

Strapi v4+ wraps payloads in a `data` object; confirm the content-type schema first.

## Sanity (GROQ / Mutations)

- Query tags (GROQ): `*[_type == "tag"] { _id, name, slug }`
- Create tag (Mutations API): `POST https://{project_id}.api.sanity.io/v2024-01-01/data/mutate/{dataset}` body `{"mutations": [{"create": {"_type": "tag", "name": "...", "slug": {"current": "..."}}}]}` with header `Authorization: Bearer {token}`

## Adapter Error-Handling Contract

Any adapter built from this reference should:

- Report which of `CMS_TYPE` / `CMS_URL` / `CMS_API_KEY` is missing, with the expected format.
- On `401`/`403`, report "Authentication failed — check CMS_API_KEY" and not retry.
- On connection timeout (~10s), report it and suggest checking `CMS_URL`.
- On duplicate slug, skip creation and note `Tag already exists: [name]`.
- On `429`, wait and retry once; report if the limit persists.
- On an unsupported `CMS_TYPE`, list the five valid platforms and stop.
