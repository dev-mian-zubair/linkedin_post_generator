
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.post import PostRequest, PostResponse
from app.schemas.template import PostTemplate
from app.services.article_parser import extract_article_content
from app.services.llm_client import generate_linkedin_post, ArticleInfo
from app.core.templates import TEMPLATES

router = APIRouter()

# GET endpoint for templates
@router.get("/templates", response_model=List[PostTemplate])
def get_templates():
  return TEMPLATES

# Update PostRequest to accept template_id
from pydantic import BaseModel
class GeneratePostRequest(BaseModel):
  url: str
  template_id: str

# Updated POST endpoint
@router.post("/generate", response_model=PostResponse)
def generate_post(data: GeneratePostRequest):
  template = next((t for t in TEMPLATES if t.id == data.template_id), None)
  if not template:
    raise HTTPException(status_code=404, detail="Template not found")
  try:
    article = extract_article_content(data.url)
    article_info = ArticleInfo(
      article_title=article["title"],
      article_text=article["text"],
      article_link=data.url,
      images=article["images"]
    )
    llm_result = generate_linkedin_post(template, article_info)
    return {
      "title": article["title"],
      "images": article["images"],
      "post_text": llm_result.get("post_text"),
      "human_post_text": llm_result.get("human_post_text"),
      "selected_image": llm_result.get("selected_image"),
      "hashtags": llm_result.get("hashtags"),
      "tone": llm_result.get("tone"),
      "template_used": template.name
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
