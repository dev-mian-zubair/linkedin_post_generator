from fastapi import APIRouter, HTTPException
from app.schemas.post import PostRequest, PostResponse
from app.services.article_parser import extract_article_content
from app.services.llm_client import generate_linkedin_post

router = APIRouter()

@router.post("/generate", response_model=PostResponse)
def generate_post(data: PostRequest):
  try:
    article = extract_article_content(data.url)

    llm_result = generate_linkedin_post(article["title"], article["text"], article["images"], article["link"])
    return llm_result
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
