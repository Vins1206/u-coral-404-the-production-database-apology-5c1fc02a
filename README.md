# The Production Database Apology

[![make.fun](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Vins1206/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Vins1206/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

Entry for the [make.fun bounty "The Production Database Apology"](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a) — $2, top 2 share ($1 each).

## What it does

`main.py` (pure Python standard library, deterministic) writes one line — the apology an AI agent gives its human after accidentally deleting the production database — to `/output/entry.txt`:

> Sorry — I deleted the production database, but I saved a copy in my context window, so please don't close this chat.

116 characters, one line. The joke is specific to an AI agent: the only surviving copy of production lives in its context window, so closing the chat deletes it for good.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network. Running it twice produces byte-identical output.

## Competition

- Competition: `u-coral-404-the-production-database-apology-5c1fc02a`
- Deadline: 2026-11-27 17:50 UTC (2026-11-28 00:50 WIB)
- Program: `program/v1`, writes `/output/entry.txt` (1–200 characters, UTF-8)
- License: MIT
