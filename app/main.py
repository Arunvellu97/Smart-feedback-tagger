from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List
from .tagger import keyword_tagger
from .store import add_feedback, list_feedback
from .llm_helper import LLMRefiner

app = FastAPI(title="Smart Feedback Tagger API")

llm = LLMRefiner()   # instantiate once (injectable in tests)

class FeedbackIn(BaseModel):
    message: str

class FeedbackOut(BaseModel):
    id: int
    message: str
    tags: List[str]

@app.post("/feedback", response_model=FeedbackOut, status_code=201)
async def create_feedback(payload: FeedbackIn):
    # 1) tag using keyword tagger (required)
    initial_tags = keyword_tagger(payload.message)

    # 2) optionally refine using llm helper (isolated)
    refined_tags = await llm.refine_tag(payload.message, initial_tags)

    # 3) store
    fb = await add_feedback(payload.message, refined_tags)
    return fb

@app.get("/feedback", response_model=List[FeedbackOut])
async def get_feedback():
    return await list_feedback()


@app.get("/")
async def root():
    return {"message": "Welcome to Smart Feedback Tagger API! Visit /docs to use the API."}
