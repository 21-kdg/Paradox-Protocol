# Consent Firewall – AI Engine

This module is the intelligence layer of the Consent Firewall.

## What it does
- Parses consent policies
- Monitors application behavior
- Detects early misuse using rule-based AI
- Classifies violations
- Makes real-time decisions

## Decisions
- ALLOW → normal access
- SANDBOX → suspicious but not critical
- BLOCK → confirmed misuse

## Why this is powerful
Even if consent exists, behavior is continuously monitored and misuse is stopped early.

## Tech
- Python
- FastAPI
- Heuristic AI (Phase 1)
