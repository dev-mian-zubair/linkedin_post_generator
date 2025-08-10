from pydantic import BaseModel, HttpUrl
from typing import List

class PostRequest(BaseModel):
    url: HttpUrl

class PostResponse(BaseModel):
    post_text: str
    human_post_text: str
    selected_image: HttpUrl
    hashtags: List[str]
    tone: str
