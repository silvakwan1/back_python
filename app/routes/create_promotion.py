from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from typing import Optional
from werkzeug.utils import secure_filename
import os
import uuid  # Para gerar um UUID único
from app.schemas.item_schema import promocoes

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def generate_unique_filename(filename: str) -> str:
    """Gera um nome de arquivo único usando UUID"""
    ext = os.path.splitext(filename)[1]  
    return secure_filename(f"{uuid.uuid4()}{ext}")  

@router.post('/create/promotion')
async def create_promotion(
    date_start: str = Form(...),
    date_end: str = Form(...),
    title: str = Form(...),
    link: Optional[str] = Form(None),
    cupom: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    categoria: str = Form(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    image: UploadFile = File(...)
):
    try:
        image_filename = generate_unique_filename(image.filename)
        file_path = os.path.join(UPLOAD_FOLDER, image_filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await image.read())
        
        promotion_id = promocoes(
            date_start,
            date_end,
            title,
            file_path,
            link,
            cupom,
            description,
            categoria,
            latitude,
            longitude
        )
        
        return {
            "newPromotion": {
                "id": promotion_id,
                "dateStart": date_start,
                "dateEnd": date_end,
                "title": title,
                "image": file_path,
                "link": link,
                "cupom": cupom,
                "description": description,
                "categoria": categoria,
                "latitude": latitude,
                "longitude": longitude
            }
        }
    except Exception as e:
        print("Erro ao salvar promoção:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao salvar promoção")
