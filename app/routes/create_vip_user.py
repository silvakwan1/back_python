from fastapi import APIRouter, HTTPException, Form
from pydantic import EmailStr
import re
from app.schemas.item_schema import vip_user

router = APIRouter()

@router.post("/create/vip-user")
async def create_vip_user(
    nome: str = Form(...),
    whatsApp: str = Form(...),
    email: EmailStr = Form(...),
):
    """
    Endpoint para criar um novo usuário VIP.
    """
    # Regex para validar número de WhatsApp no formato E.164
    whatsApp_regex = re.compile(r"^\+?[1-9]\d{1,14}$")
    
    # Verificação do formato do WhatsApp
    if not whatsApp_regex.match(whatsApp):
        raise HTTPException(status_code=400, detail="O formato do WhatsApp está inválido. Use o formato internacional com código do país.")

    try:
        vip_user(nome, whatsApp, email)

        return {"message": "Usuário VIP criado com sucesso"}
    except Exception as e:
        print("Erro ao criar usuário VIP:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao criar usuário VIP")
