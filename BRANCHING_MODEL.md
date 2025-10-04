# Branching and Version Control Strategy

## Overview
This repository follows a simplified GitFlow model supporting three environments: DEV, UAT, and PROD.

## Branches

- **main** → Production branch. Only stable, tested code.
- **develop** → Active development branch integrated with DEV environment.
- **release/** → Candidate versions promoted to UAT.
- **feature/** → New features or fixes under development.
- **hotfix/** → Critical fixes for production.

## Workflow

1. Create a feature branch from `develop`.
2. Commit and push changes to the feature branch.
3. Open a Pull Request (PR) to merge into `develop`.
4. When `develop` is stable, create `release/x.y.z`.
5. Test `release/x.y.z` in UAT; after approval, merge into `main`.
6. Tag `main` with version and deploy to PROD.

## Naming Conventions
- `feature/<short-description>`
- `bugfix/<short-description>`
- `release/v<version>`
- `hotfix/<short-description>`
