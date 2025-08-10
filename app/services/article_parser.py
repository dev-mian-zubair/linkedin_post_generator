from newspaper import Article

def extract_article_content(url: str):
  article = Article(str(url))
  try:
    article.download()
    article.parse()
    return {
      "title": article.title,
      "text": article.text,
      "images": list(article.images),  # Convert set → list
      "link": article.canonical_link
    }
  except Exception as e:
    # Handle network errors, DNS failures, etc.
    return {
      "error": f"Failed to download or parse article from {url}. Reason: {str(e)}"
    }
