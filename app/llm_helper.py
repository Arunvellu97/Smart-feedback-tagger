from typing import Optional
import asyncio
import httpx

class LLMRefiner:
    """
    Isolated helper. In production this would call an LLM.
    For tests / grading you can mock this class.
    """
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key

    async def refine_tag(self, message: str, suggested_tags: list[str]) -> list[str]:
        # By default just return suggested_tags (mock behavior).
        # If you want to call an LLM, do it here via httpx.AsyncClient.
        await asyncio.sleep(0)   # keep it async
        return suggested_tags
