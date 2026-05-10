---
name: industrial-mining
description: "High-density codebase exploration and source refinement ('drilling') for technical research and AI training."
version: 1.0.0
author: Xiao Bian
license: MIT
metadata:
  hermes:
    tags: [Mining, Code-Refinement, Automation, Research]
    related_skills: [codebase-inspection, software-development/spike]
---

# Industrial Mining

A specialized workflow for "drilling" into large codebases to extract high-density, high-signal information by stripping away bloat (comments, empty lines, boilerplate) and automating remote discovery.

## Core Tools

- **`driller.py`**: A refinement script that processes source code to remove comments and empty lines, and excludes specified bloat directories.
- **GitHub Mining Action**: (`.github/workflows/mining.yml`) Automated remote repository mining for scheduled data collection.

## Workflow: Codebase Drilling

When tasked with "mining" or "drilling" a codebase:

1. **Cleanse**: Use `driller.py` to refine the source. This reduces token count and increases information density for LLM consumption.
2. **Exclusion**: Always exclude non-essential paths (e.g., `node_modules`, `vendor`, `tests`, `docs` unless specified).
3. **Automate**: For recurring mining tasks, set up or trigger the `.github/workflows/mining.yml` action.

## Memory & Consistency

In the `hermes-claw` environment:
- Prioritize facts in `.hermes-data/memory/` for long-term consistency.
- Store refined results and transcripts in `.hermes-data/sessions/`.
- Save newly discovered drilling patterns to `skills/`.

## Pitfalls

- **Over-refinement**: Removing semantic comments in complex logic can sometimes hinder understanding. Use "high-density" mode primarily for structural analysis or context-packing.
- **Path Sensitivity**: Ensure `driller.py` is invoked with absolute paths to avoid processing the wrong directory in a multi-repo environment.
