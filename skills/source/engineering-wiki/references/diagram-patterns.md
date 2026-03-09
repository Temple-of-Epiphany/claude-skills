# Diagram Patterns Reference

**Version:** 1.0.0
**Date Created:** 2026-03-08
**Author:** Colin Bitterfield

Mermaid diagram patterns used in the TapMe Contact engineering wiki. Copy-paste these and adapt for any new diagrams.

---

## Rules

1. **Mermaid only** — GitHub wiki renders Mermaid natively. No GraphViz, no PlantUML, no external image services.
2. All diagrams go in fenced code blocks with `mermaid` as the language tag.
3. Use subgraphs with emoji+label headers to communicate tier/layer.
4. Explicitly show which network/tunnel inter-service calls traverse.
5. Dashed lines (`-.->`) for external/optional dependencies; solid lines (`-->`) for required paths.

---

## Color/Emoji Tier Convention

| Tier | Emoji | Label Example | Used In |
|------|-------|---------------|---------|
| External | 🌐 | `External["🌐 External"]` | Internet users, external services |
| Edge/Proxy | 🔵 | `Edge["🔵 Edge Layer"]` | Traefik, Certbot |
| Customer Frontend | 🟢 | `CustomerFE["🟢 Customer Frontend"]` | tapme-site, tapme-app |
| Customer Backend | 🔴 | `CustomerBE["🔴 Customer Backend"]` | tapme-api |
| Employee Frontend | 🟡 | `EmployeeFE["🟡 Employee Frontend"]` | tapme-admin |
| Employee Backend | 🟠 | `EmployeeBE["🟠 Employee Backend"]` | tapme-admin-api |
| Auth | 🔒 | `Auth["🔒 Authentication"]` | FusionAuth, Elasticsearch |
| Data | 🟣 | `Data["🟣 Data Layer"]` | PostgreSQL, Redis |
| Monitoring | 📊 | `Monitoring["📊 Monitoring"]` | Grafana, Prometheus, Uptime Kuma |
| Infrastructure | ⚙️ | `Infra["⚙️ Infrastructure"]` | tapme-infra, tapme-traefik |

---

## Pattern 1: Service Architecture (graph TB)

Full platform architecture showing all tiers and inter-service communication.

```mermaid
graph TB
    subgraph External["🌐 External"]
        Users["Internet Users"]
        NFC["NFC Card Tap"]
        Stripe["Stripe Payments"]
    end

    subgraph Edge["🔵 Edge Layer — Ports 80/443"]
        Traefik["Traefik v2.11<br/>Reverse Proxy<br/>SSL Termination"]
    end

    subgraph CustomerFE["🟢 Customer Frontend — traefik_proxy network"]
        Site["tapme-site<br/>Marketing Website<br/>Next.js :3000"]
        App["tapme-app<br/>Customer Portal<br/>Next.js :3002"]
    end

    subgraph CustomerBE["🔴 Customer Backend — internal + db_network"]
        API["tapme-api<br/>Customer FastAPI<br/>:8000"]
    end

    subgraph Auth["🔒 Authentication — traefik_proxy + internal"]
        FusionAuth["FusionAuth<br/>Identity Provider<br/>:9011"]
    end

    subgraph Data["🟣 Data Layer — db_network only"]
        PG["PostgreSQL 16<br/>:5432"]
        Redis["Redis<br/>:6379"]
    end

    Users -->|"HTTPS :443"| Traefik
    NFC -->|"HTTPS /view?id=xxx"| Traefik
    Traefik -->|"tapme.contact"| Site
    Traefik -->|"account.*"| App
    Traefik -->|"api.*"| API
    Traefik -->|"auth.*"| FusionAuth
    Site -.->|"REST"| API
    App -.->|"Management"| API
    API -->|"tapme_api role"| PG
    API --> Redis
    Site -.->|"Payments"| Stripe
```

---

## Pattern 2: Security Boundary (graph LR)

Shows the hard security boundary between customer and employee tiers. Include JWT rejection explicitly.

```mermaid
graph LR
    subgraph Customer["🟢 Customer Tier"]
        C_FE["tapme-site / tapme-app"]
        C_API["tapme-api :8000"]
        C_JWT["JWT aud: {customer-app-uuid}"]
        C_DB["DB role: tapme_api<br/>cards rw, store ro"]
    end

    subgraph Employee["🟡 Employee Tier"]
        E_FE["tapme-admin :3010"]
        E_API["tapme-admin-api :8010"]
        E_JWT["JWT aud: {admin-app-uuid}"]
        E_DB["DB role: tapme_admin_api<br/>cards rw, store rw, admin rw"]
    end

    C_FE --> C_API
    C_API --- C_JWT
    C_API --- C_DB

    E_FE --> E_API
    E_API --- E_JWT
    E_API --- E_DB

    C_JWT -.->|"REJECTED"| E_API
    E_JWT -.->|"REJECTED"| C_API
```

---

## Pattern 3: CI/CD Pipeline (graph LR)

Shows build, test, security scan, and sequential rolling deploy.

```mermaid
graph LR
    subgraph Trigger["🟡 Trigger"]
        Dev["Developer<br/>Commit"]
        GH["GitHub<br/>Repository"]
    end

    subgraph Test["🟢 Test"]
        Lint["Lint"]
        Unit["Unit Tests"]
        Int["Integration Tests"]
    end

    subgraph Security["🔴 Security"]
        Aikido["Aikido SAST + DAST"]
        Secrets["Secrets Detection"]
    end

    subgraph Build["🔵 Build"]
        Docker["Docker Build<br/>Multi-stage"]
        Push["Push to GHCR"]
    end

    subgraph Deploy["🟣 Deploy"]
        Migrate["Alembic migrate<br/>(API only)"]
        N0["node0<br/>Sequential"]
        N1["node1<br/>Sequential"]
    end

    Dev --> GH --> Lint --> Unit --> Int
    Int --> Aikido --> Secrets --> Docker --> Push
    Push --> Migrate --> N0 --> N1
```

---

## Pattern 4: Physical Topology (graph TB)

Shows VPS hosts, WireGuard VPN, Cloudflare routing, service placement.

```mermaid
graph TB
    subgraph Internet["🌐 Internet"]
        Users["Users"]
        CF["Cloudflare<br/>Geo-routing + Health Checks"]
    end

    subgraph VA["☁️ Virginia (dev-node0) — 10.10.0.1"]
        T_VA["Traefik :443"]
        Services_VA["All Services<br/>Customer + Employee + Data"]
    end

    subgraph OR["☁️ Oregon (VPS-OR) — 10.10.0.2"]
        T_OR["Traefik :443"]
        Services_OR["Customer Services Only<br/>tapme-site, tapme-app, tapme-api"]
    end

    subgraph MON["☁️ Virginia-MON (VPS-MON) — 10.10.0.3"]
        Uptime["Uptime Kuma"]
        Grafana["Grafana + Prometheus"]
    end

    Users --> CF
    CF -->|"geo-route"| T_VA
    CF -->|"geo-route"| T_OR
    VA <-->|"WireGuard 10.10.0.0/24"| OR
    VA <-->|"WireGuard"| MON
    OR <-->|"WireGuard"| MON
```

---

## Pattern 5: User Journey (sequenceDiagram)

For NFC tap, purchase, login, and other multi-step flows.

```mermaid
sequenceDiagram
    participant User
    participant Browser
    participant Traefik
    participant API as tapme-api
    participant DB as PostgreSQL
    participant Redis

    User->>Browser: Tap NFC card
    Browser->>Traefik: GET /view?id={md5_hash}
    Traefik->>API: GET /view?id={md5_hash}
    API->>Redis: GET cache:device:{md5_hash}
    alt Cache hit
        Redis-->>API: destination URL
    else Cache miss
        API->>DB: SELECT destination FROM devices WHERE md5_hash=?
        DB-->>API: destination URL
        API->>Redis: SET cache:device:{md5_hash} (TTL 300s)
    end
    API-->>Browser: 302 Redirect to destination
    API->>DB: INSERT INTO tap_events (device_id, ip, ua, ts)
```

---

## Pattern 6: Service Tier Map (graph TB)

Simplified view organizing repos into tiers.

```mermaid
graph TB
    subgraph Infra["⚙️ Infrastructure Tier"]
        engineering["tapme-engineering<br/>Docs only"]
        infra["tapme-infra<br/>Host-level setup"]
        traefik["tapme-traefik<br/>Reverse proxy"]
    end

    subgraph Customer["🟢 Customer Tier"]
        site["tapme-site<br/>Site + Store"]
        app["tapme-app<br/>Customer Portal"]
        api["tapme-api<br/>Customer API"]
    end

    subgraph Employee["🟡 Employee Tier"]
        admin["tapme-admin<br/>Employee portal"]
        adminapi["tapme-admin-api<br/>Employee API"]
    end

    subgraph Data["🟣 Data Tier"]
        sql["tapme-sql<br/>PostgreSQL"]
        redis["tapme-redis<br/>Redis"]
        fa["tapme-fusion-auth<br/>FusionAuth"]
    end

    subgraph Mon["📊 Monitoring Tier"]
        uptime["tapme-uptime<br/>Uptime Kuma"]
        grafana["tapme-grafana<br/>Grafana + Prometheus"]
    end

    traefik --> site & app & api & admin & adminapi & fa
    site & app & api --> sql & redis & fa
    admin & adminapi --> sql & redis & fa
    grafana --> api & adminapi & traefik
    uptime --> traefik
```

---

## Common Mistakes to Avoid

1. **Don't use `graph TD` and `graph TB` inconsistently** — pick one and use it for the same page. `TB` = top-bottom, `TD` = top-down, they are identical.
2. **Don't mix `-->` and `-.->` without meaning** — solid = required/primary, dashed = optional/external/read-only.
3. **Don't skip the `subgraph` for tiers** — isolation of tiers is the main value of architecture diagrams.
4. **Don't use bare node IDs** — always give nodes descriptive labels with the pattern `ID["Label<br/>detail"]`.
5. **Don't draw the monitoring connections inline with services** — keep Prometheus/Grafana/Uptime Kuma in their own subgraph and connect from there.
6. **Don't omit the network name** from edge labels when it's non-obvious (e.g., `-->|"WireGuard tunnel"| node`).
