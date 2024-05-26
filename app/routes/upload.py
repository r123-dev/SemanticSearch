from fastapi import APIRouter, UploadFile, File
from app.services.pdf_extraction import extract_text_from_pdf
from app.services.embedding import create_embedding, add_to_index
import os

upload_router = APIRouter()

UPLOAD_DIR = 'uploaded_files'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@upload_router.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(file.file.read())
    
    text = extract_text_from_pdf(file_location)
    embedding = create_embedding(text)
    add_to_index(embedding, file.filename)
    
    return {"filename": file.filename}
