import json
import google.generativeai as genai
from app.core.config import settings
from app.schemas.template import PostTemplate
from pydantic import BaseModel

class ArticleInfo(BaseModel):
  article_title: str
  article_text: str
  article_link: str
  images: list[str]

# Initialize the Generative AI client
genai.configure(api_key=settings.GEMINI_API_KEY)

# Function to build the prompt
def build_prompt(template: PostTemplate, article: ArticleInfo):
    prompt_parts = [
      "You are a professional LinkedIn content creator.",
      template.prompt,
    ]

    if template.hook_required:
      prompt_parts.append("- Start with an engaging hook in the first sentence.")
    if template.include_article_link:
      prompt_parts.append(f"- Naturally include this link: {article.article_link}")
    if template.select_best_image:
      if article.images:
        prompt_parts.append("- Pick the MOST relevant image from the list.")
      else:
        prompt_parts.append("- No relevant image found in the article. Search the web for a highly relevant image and return its direct URL as 'selected_image'.")
    if template.detect_tone:
      prompt_parts.append("- Detect and label the tone.")
    if template.generate_human_post:
      prompt_parts.append(
        "- Create a second version 'human_post_text' that rewrites the post in a simple, humanistic style."
      )
    if template.style_guidelines:
      prompt_parts.append(f"- Follow this style guideline: {template.style_guidelines}")

    prompt_parts.append(f"- Generate {template.hashtag_count} relevant hashtags.")
    if template.hashtags:
      prompt_parts.append(f"- Prefer hashtags from: {', '.join(template.hashtags)}")

    # INPUT section
    prompt_parts.append(f"""
INPUT:
Title: {article.article_title}
Content: {article.article_text[:3000]}
Article Link: {article.article_link}
Images: {article.images}
""")

    # OUTPUT section
    prompt_parts.append("""
OUTPUT:
Return ONLY valid JSON with:
- post_text (string)
- human_post_text (string)
- selected_image (string URL)
- hashtags (list of strings)
- tone (string)
""")

    return "\n".join(prompt_parts)

# Function to generate the post
def generate_linkedin_post(template: PostTemplate, article: ArticleInfo):
    prompt = build_prompt(template, article)

    model = genai.GenerativeModel(settings.MODEL_NAME)
    response = model.generate_content(prompt)

    print(response)

    # Clean response: remove code block markers and extra text
    resp_text = response.text.strip()
    if resp_text.startswith('```json'):
        resp_text = resp_text[len('```json'):].strip()
    if resp_text.startswith('```'):
        resp_text = resp_text[len('```'):].strip()
    if resp_text.endswith('```'):
        resp_text = resp_text[:-len('```')].strip()

    try:
        return json.loads(resp_text)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON")
