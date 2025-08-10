from fastapi import FastAPI
from app.api import post

app = FastAPI(title="LinkedIn Post Generator")
app.include_router(post.router)
