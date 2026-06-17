# SmartApply

AI-powered resume analyzer that scores candidate fit against job descriptions using structured LLM output.

## What it does
- Analyzes a resume against a job description
- Returns a match score (0-100), strengths, skill gaps, and a rewritten resume summary
- Uses OpenAI structured output with Pydantic validation

## Tech stack
Python · FastAPI · OpenAI API · Pydantic · uv

## Setup
1. Clone the repo
2. Run `uv sync`
3. Copy `.env.example` to `.env` and add your OpenAI API key
4. Run `python -m uvicorn app.main:app --reload`

## Project structure
- `app/services/` — LLM logic and retry handling
- `app/models.py` — Pydantic input/output schemas
- `app/utils/` — configuration, exceptions, prompts