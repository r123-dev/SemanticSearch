from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.embedding import search_embeddings

search_router = APIRouter()

@search_router.get("/docs")
async def search_docs(q: str):
    results = search_embeddings(q)
    return JSONResponse(content={"results": results})
