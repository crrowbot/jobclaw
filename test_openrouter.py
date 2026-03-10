#!/usr/bin/env python3
"""Test OpenRouter connectivity with JobClaw's LLMMatcher."""

import asyncio
import os
from pathlib import Path

# Ensure we're using the project's virtual environment
import sys
sys.path.insert(0, str(Path(__file__).parent / ".venv" / "lib" / "python3.11" / "site-packages"))

from jobclaw.domain import Job, JobSource, Profile, SalaryRange
from jobclaw.matcher.llm_matcher import LLMMatcher

# Sample job and profile for testing
sample_job = Job(
    title="Senior Python Developer",
    description="We are looking for a senior Python developer with experience in FastAPI, async programming, and cloud services. Must have 5+ years experience.",
    company="TechCorp Inc",
    location="Remote",
    url="https://example.com/job1",
    source=JobSource.BOSS,  # Use a valid source
    salary=SalaryRange(min_annual=150000, max_annual=200000, currency="USD"),
    tags=["python", "fastapi", "async", "cloud"],
)

sample_profile = Profile(
    name="John Doe",
    skills=["Python", "FastAPI", "asyncio", "AWS", "Docker"],
    years_experience=6.0,
    summary="Senior software engineer specializing in Python backend development.",
)

async def test_match():
    matcher = LLMMatcher()
    print(f"Testing with backend: {matcher._backend}, model: {matcher._model_name}")

    try:
        result = await matcher.match(sample_job, sample_profile)
        print("\n✅ Match successful!")
        print(f"Score: {result.score}/10")
        print(f"Reasoning: {result.reasoning[:200]}...")
        return True
    except Exception as e:
        print(f"\n❌ Match failed: {type(e).__name__}: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_match())
    sys.exit(0 if success else 1)
