from fastapi import FastAPI
from app.routes.upload import upload_router
from app.routes.search import search_router

app = FastAPI()

app.include_router(upload_router, prefix="/api")
app.include_router(search_router, prefix="/api")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
