from pydantic import BaseModel, Field
from typing import Optional

# What the user sends TO the app
class AnalysisRequest(BaseModel):
    resume: str = Field(
        min_length=50,
        description="The candidate's full resume text"
    )
    job_description: str = Field(
        min_length=50,
        description="The full job description to match against"
    )

# What the app sends BACK to the user
class AnalysisResult(BaseModel):
    match_score: int = Field(
        ge=0,           # greater than or equal to 0
        le=100,         # less than or equal to 100
        description="Overall match percentage between resume and job description"
    )
    summary: str = Field(
        min_length=10,
        description="One paragraph overall assessment"
    )
    strengths: list[str] = Field(
        min_length=1,
        description="What the resume does well for this role"
    )
    gaps: list[str] = Field(
        description="Skills or experience missing from the resume"
    )
    rewritten_summary: str = Field(
        min_length=10,
        description="Improved resume summary section"
    )
    # present only when relevant
    recommendation: Optional[str] = Field(
    default=None,
    description="Specific action recommendation when the match score is below 60"
)