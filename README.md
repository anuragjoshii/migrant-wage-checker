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

**Watch Hackathon Demo Video:** https://youtu.be/8jMNG8o9Yf4


## Data Analysis
A supporting Python script (wage_gap_analysis.py) analyzes the wage dataset directly. It finds a 2.83x disparity between the highest-paying state (Karnataka, ~₹832/day avg) and the lowest-paying state (Rajasthan, ~₹294/day avg) in this sample for the same categories of work. It also produces an illustrative estimate (assumptions stated in the script) that if roughly 30% of India's ~10 crore migrant workers are underpaid by even ₹150/day, that could amount to a potential ₹1,40,400 crore/year in wage theft nationally. See state_wage_gap_chart.png for the visual breakdown by state.
This estimate is explicitly a scale-illustrating calculation, not a measured statistic — it exists to communicate why an accessible wage-checking tool matters at national scale.
## Tools and AI Assistance Used
- **PartyRock (Amazon Bedrock)** — no-code app builder for the core wage-checking tool.

- **Claude (Anthropic)** — used for project planning, drafting documentation, and writing/reviewing the wage_gap_analysis.py script.


- All data compilation, testing, and final decisions were done by me.

---

*Built solo in 3 days for First Commit, Bharat Builds Tour.*
