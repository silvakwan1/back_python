from fastapi import APIRouter, HTTPException, Query
from app.database import cursor, conn  
from datetime import datetime, date
import os

UPLOAD_FOLDER = "uploads"

def deletar_promocoes_expiradas():
    """Deleta as promoções cujo 'date_end' já passou e remove a imagem do servidor"""
    try:
        data_atual = date.today()
        
        cursor.execute("SELECT id, dateEnd, image FROM Promocoes WHERE dateEnd < %s", (data_atual,))
        promocoes = cursor.fetchall()

        for promocao in promocoes:
            promo_id, date_end, image_path = promocao
            
            if image_path:
                full_path = os.path.join(UPLOAD_FOLDER, image_path)
                if os.path.exists(full_path):
                    try:
                        os.remove(full_path)
                        print(f"Imagem {full_path} da promoção {promo_id} deletada com sucesso.")
                    except OSError as e:
                        print(f"Erro ao deletar imagem {full_path}: {e}")
            
            cursor.execute("DELETE FROM Promocoes WHERE id = %s", (promo_id,))
            print(f"Promoção com id {promo_id} deletada porque passou da data de término.")

        conn.commit()
        
        return {"message": f"Deletadas {len(promocoes)} promoções expiradas"}
        
    except Exception as e:
        print(f"Erro ao deletar promoções expiradas: {e}")
        conn.rollback()
        raise HTTPException(
            status_code=500, 
            detail=f"Erro interno ao deletar promoções expiradas: {str(e)}"
        )