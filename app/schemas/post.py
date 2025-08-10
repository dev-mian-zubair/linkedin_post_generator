from pydantic import BaseModel, HttpUrl
from typing import List

class PostRequest(BaseModel):
    url: HttpUrl

class PostResponse(BaseModel):
    title: str
    images: List[HttpUrl]
    post_text: str
    human_post_text: str
    selected_image: str
    hashtags: List[str]
    tone: str
    template_used: str
