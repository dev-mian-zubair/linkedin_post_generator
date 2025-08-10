from pydantic import BaseModel
from typing import List, Optional

class PostTemplate(BaseModel):
    id: str
    name: str
    description: str
    prompt: str  # LLM instruction
    hashtags: Optional[List[str]] = None
    cta: Optional[str] = None

    # New metadata for richer generation
    hook_required: bool = True
    include_article_link: bool = True
    hashtag_count: int = 8
    detect_tone: bool = True
    generate_human_post: bool = True
    select_best_image: bool = True
    style_guidelines: Optional[str] = None  # e.g., "Conversational & inspiring"
