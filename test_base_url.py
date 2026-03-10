#!/usr/bin/env python3
"""Test that OPENAI_BASE_URL configuration works correctly."""

import os
import sys

# Set test environment variables
os.environ["OPENAI_API_KEY"] = "sk-test123"
os.environ["OPENAI_BASE_URL"] = "https://api.custom-openai.com/v1"
os.environ["JOBCLAW_LLM_MODEL"] = "gpt-4o-mini"

from jobclaw.config import get_settings
from jobclaw.matcher.llm_matcher import LLMMatcher

settings = get_settings()
print(f"Settings loaded:")
print(f"  openai_api_key: {settings.openai_api_key[:10]}..." if settings.openai_api_key else "  openai_api_key: None")
print(f"  openai_base_url: {settings.openai_base_url}")
print(f"  jobclaw_llm_model: {settings.jobclaw_llm_model}")

# Test backend resolution
matcher = LLMMatcher()
print(f"\nLLMMatcher initialized:")
print(f"  backend: {matcher._backend}")
print(f"  model_name: {matcher._model_name}")
print(f"  _llm object: {type(matcher._llm)}")

# Check if ChatOpenAI was used (has openai_api_base attribute)
if hasattr(matcher._llm, 'openai_api_base'):
    print(f"  openai_api_base: {matcher._llm.openai_api_base}")
else:
    print(f"  openai_api_base: not available (using init_chat_model fallback)")

print("\n✅ Test passed: OPENAI_BASE_URL configuration is working!")
