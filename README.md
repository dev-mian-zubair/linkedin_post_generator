
# LinkedIn Post Generator

Generate professional, humanistic, and template-driven LinkedIn posts from articles using LLMs and NLP techniques.

## Features
- Extracts article content from a URL
- Template system: users select a post style (e.g., Insight, Storytelling, Debate, etc.)
- Summarizes and rewrites content for LinkedIn
- Generates hashtags, detects tone, and selects or finds relevant images
- If no image is found in the article, the LLM will search the web for a suitable image
- Provides both professional and humanistic versions of the post

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API keys in `app/core/config.py`
4. Run the FastAPI server: `uvicorn app.main:app --reload`

## API Endpoints
- `GET /templates` — List available post templates for user selection
- `POST /generate` — Generate a LinkedIn post from an article URL and selected template

### Example POST /generate Request
```
{
	"url": "https://example.com/article",
	"template_id": "insight"
}
```

### Example Response
```
{
	"title": "...",
	"images": ["..."],
	"post_text": "...",
	"human_post_text": "...",
	"selected_image": "...",
	"hashtags": ["..."],
	"tone": "...",
	"template_used": "Industry Insight"
}
```

## Folder Structure
- `app/api/` — API routes
- `app/services/` — LLM client, article parsing
- `app/schemas/` — Pydantic schemas for requests, responses, templates
- `app/core/` — Configuration and template definitions

## Requirements
See `requirements.txt` for dependencies.

## License
MIT
