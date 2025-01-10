import os
from fastapi import APIRouter, HTTPException, Path
from app.database import cursor, conn

router = APIRouter()

@router.delete("/promocoes/delete/{id}")
async def delete_promotion(id: int = Path(..., description="ID da promoção a ser deletada")):
    """
    Endpoint para deletar uma promoção pelo ID.
    """
    try:
        cursor.execute("SELECT id, image FROM Promocoes WHERE id = %s", (id,))
        promotion = cursor.fetchone()

        if not promotion:
            raise HTTPException(status_code=404, detail="Promoção não encontrada.")

        promo_id, image_path = promotion

        if image_path:
            full_path = os.path.normpath(image_path)

            if not os.path.isabs(full_path):
                full_path = os.path.join(os.getcwd(), full_path)

            print(f"Caminho final da imagem: {full_path}")

            if os.path.exists(full_path):
                try:
                    os.remove(full_path)  
                    print(f"Imagem {full_path} da promoção {promo_id} deletada com sucesso.")
                except OSError as e:
                    print(f"Erro ao deletar imagem {full_path}: {e}")
                    raise HTTPException(
                        status_code=500,
                        detail=f"Erro ao deletar imagem: {str(e)}"
                    )
            else:
                print(f"O arquivo {full_path} não existe.")

        # Deletar a promoção do banco de dados
        cursor.execute("DELETE FROM Promocoes WHERE id = %s", (promo_id,))
        conn.commit()
        return {"message": f"Promoção com ID {promo_id} deletada com sucesso."}


    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        conn.rollback()
        print(f"Erro ao deletar promoção: {e}")
        raise HTTPException(
            status_code=500,
            detail=f"Erro interno ao deletar promoção: {str(e)}"
        )
