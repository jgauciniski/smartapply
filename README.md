# SmartApply

AI-powered resume analyzer that scores candidate fit against job descriptions using structured LLM output.

## What it does
- Analyzes a resume against a job description
- Returns a match score (0-100), strengths, skill gaps, and a rewritten resume summary
- Uses OpenAI structured output with Pydantic validation
- Validates input content (not just structure) before calling the LLM, with custom exception handling and correct HTTP status codes

## Tech stack
Python · FastAPI · OpenAI API · Pydantic · uv · pytest

## API Endpoints

**`GET /health`**
Returns `{"status": "OK"}`. Used for deployment health checks.

**`POST /analyze`**
Accepts a resume and job description, returns a structured analysis.

Request body:
```json
{
  "resume": "...",
  "job_description": "..."
}
```

Response:
```json
{
  "match_score": 85,
  "summary": "...",
  "strengths": ["..."],
  "gaps": ["..."],
  "rewritten_summary": "...",
  "recommendation": "..."
}
```

Returns `422` for invalid input (empty or whitespace-only fields), `500` if the LLM analysis fails after retries.

Interactive API docs available at `/docs` once the server is running.

## Setup
1. Clone the repo
2. Run `uv sync`
3. Copy `.env.example` to `.env` and add your OpenAI API key
4. Run `uvicorn app.main:app --reload`
5. Visit `http://127.0.0.1:8000/docs` to explore and test the API

## Running tests
```bash
pytest tests/ -v
```
The LLM call is mocked in tests — no API calls are made and no tokens are spent. 6 tests covering Pydantic model validation, input guards, and service behavior.

## Project structure
- `app/main.py` — FastAPI routes and exception handlers
- `app/models.py` — Pydantic input/output schemas
- `app/services/` — LLM logic (`llm.py`) and orchestration with retry handling (`analyzer.py`)
- `app/utils/` — configuration, custom exceptions, prompts
- `tests/` — pytest suite with mocked LLM calls