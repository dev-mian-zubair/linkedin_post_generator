import json
import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_linkedin_post(article_title: str, article_text: str, images: list[str], article_link: str = None):
    prompt = f"""
You are a professional LinkedIn content creator.
I will give you an article title, text, article link, and a list of image URLs.

TASK:
- Summarize the article into a compelling LinkedIn post.
- Include an engaging hook in the first sentence.
- Make it professional but engaging for LinkedIn readers.
- Pick the MOST relevant image from the list.
- Generate 5-8 relevant hashtags.
- Detect and label the tone (e.g., Professional, Inspirational, Informative).
- IMPORTANT: After generating the post text, create a second version called 'human_post_text' that rewrites the post in a simple, humanistic style as if a real person is writing. Use techniques similar to Quillbot to make the language natural, clear, and easy to read. Avoid overly formal or robotic language. Do not use placeholders like [Link to Article] or [More Info]; instead, directly include the actual link or information in the post text where appropriate.

INPUT:
Title: {article_title}
Content: {article_text[:3000]}  # truncated for token limit
Article Link: {article_link}
Images: {images}

OUTPUT:
Return ONLY valid JSON with the following keys:
- post_text (string)
- human_post_text (string, a simple, humanistic rewrite of post_text with direct links or information, no placeholders)
- selected_image (string URL from the given images)
- hashtags (list of strings)
- tone (string)
"""

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
