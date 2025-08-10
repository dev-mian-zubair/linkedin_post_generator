# LinkedIn Post Generator

This project generates professional and humanistic LinkedIn posts from articles using LLMs and NLP techniques.

## Features
- Extracts article content from a URL
- Summarizes and rewrites content for LinkedIn
- Generates hashtags, selects relevant images, and detects tone
- Provides both professional and humanistic versions of the post

## Usage
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your API keys in the configuration
4. Run the FastAPI server

## API Endpoints
- `/generate` - Generate a LinkedIn post from an article URL

## Folder Structure
- `app/api/` - API routes
- `app/services/` - Core logic (LLM, article parsing)
- `app/schemas/` - Pydantic schemas
- `app/core/` - Configuration

## Requirements
See `requirements.txt` for dependencies.

## License
MIT
