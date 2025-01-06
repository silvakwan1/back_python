from fastapi import APIRouter, HTTPException
from app.database import cursor  # Supondo que você tenha o cursor configurado no database.py

router = APIRouter()

@router.get('/promotions')
async def get_all_promotions():
    try:
        # Executar a consulta para obter todas as promoções
        cursor.execute("SELECT * FROM Promocoes")
        promotions = cursor.fetchall()

        # Estruturar o resultado em uma lista de dicionários
        all_promotions = []
        for promotion in promotions:
            all_promotions.append({
                "id": promotion[0],
                "dateStart": promotion[1],
                "dateEnd": promotion[2],
                "title": promotion[3],
                "image": promotion[4],
                "link": promotion[5],
                "cupom": promotion[6],
                "description": promotion[7],
                "categoria": promotion[8],
                "latitude": promotion[9],
                "longitude": promotion[10],
                "createdAt": promotion[11]
            })

        return {"promotions": all_promotions}

    except Exception as e:
        print("Erro ao buscar promoções:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao buscar promoções")
