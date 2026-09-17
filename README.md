# Migrant Wage Checker

**Built for:** First Commit — Bharat Builds Tour (AWS x WeMakeDevs Hackathon), September 2026
**Track:** Build It (Open source / PartyRock)
**Built by:** Anurag Joshi

---

## The Problem

India has over 10 crore internal migrant workers — people who travel from their home state to work in construction, agriculture, factories, and domestic work in another state. Minimum wage in India is not a single national number. Every state sets its own rate, split further by job category and skill level (unskilled, semi-skilled, skilled). A worker doing the same job can legally be owed anywhere from ₹285/day to ₹1,050/day depending on which state they're in.

Most migrant workers have no easy way to check what they are actually owed. They don't know:
- What the minimum wage is for their state and job type
- Whether they are being underpaid
- Where to go if they are being cheated

Employers exploit this information gap. Wage theft against migrant labour is a widespread, well-documented problem in India — and it persists largely because the information needed to catch it is scattered across state labour department notifications that an ordinary worker will never read.

## The Solution

**Migrant Wage Checker** is a simple, no-code AI tool where a worker (or anyone helping them) enters:
1. Their state
2. Their job category (construction, agriculture, domestic work, factory work)
3. Their skill level
4. What they are actually being paid per day

The app looks up the applicable state minimum wage, compares it to what the worker is actually receiving, and responds in simple, bilingual (Hindi + English) language:
- Confirms whether they are being paid fairly
- If underpaid, explains the shortfall in plain terms
- Points them to the Labour Department helpline to file a complaint

No login, no jargon, no legal reading required — just a direct answer, in a language most migrant workers are comfortable reading.

## How It's Built

- **Amazon Bedrock (via PartyRock)** — the AI reasoning layer that reads the wage data, compares it against user input, and generates the plain-language bilingual response.
- **PartyRock** — used as the no-code app builder: input widgets (state, job type, skill level, actual wage) feed into a data lookup + AI response widget, hosted and shared as a public link, no servers managed manually.
- **Data:** a compiled reference table (`minimum_wage_data.csv`) of state-wise minimum wage rates across major job categories, based on state labour department notifications (2026 rates).

This is a demo-scale prototype: the wage table covers major states and common job categories as a proof of concept. A production version would pull live rates directly from state labour department portals and expand to all scheduled employments.

## What I Learned

This was my first time building with Amazon Bedrock / PartyRock. The biggest learning was how much can be done by describing intent in plain language to a foundation model instead of writing lookup/comparison logic by hand — the AI widget handles the data matching and bilingual tone of the response, which normally would need custom backend code.

## Files in This Repo

- `README.md` — this file
- `minimum_wage_data.csv` — state-wise minimum wage reference data used by the app
- `prompts.md` — the exact PartyRock prompts used to build the app
- `screenshots/` — screenshots of the working app

## Live Demo

**Try it here:** [Migrant Worker Fair Pay Checker](https://partyrock.aws/u/anuragjoshiii/ngeqGaRSs/Migrant-Worker-Fair-Pay-Checker)

**Note:** PartyRock requires a free Amazon sign-in (no credit card) to run the AI — this is standard for all PartyRock apps.

## Demo Video

**Watch here:** [Video link — paste here]

---

*Built solo in 3 days for First Commit, Bharat Builds Tour.*
