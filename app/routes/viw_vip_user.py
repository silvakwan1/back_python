from fastapi import APIRouter, HTTPException
from app.database import cursor  
router = APIRouter()

@router.get("/vip-users")
async def get_vip_users():
    """
    Endpoint para buscar todos os usuários VIP.
    """
    try:
       
        cursor.execute("SELECT * FROM VipUsers")
        vip_users = cursor.fetchall()

        all_vipUser = []
        for vip_user in vip_users:

            all_vipUser.append({
                "id": vip_user[0],
                "nome": vip_user[1],
                "email": vip_user[2],
                "whatsApp": vip_user[3],
            })

        return  all_vipUser

    except Exception as e:
        print("Erro ao buscar usuários VIP:", e)
        raise HTTPException(status_code=500, detail="Erro ao buscar usuários VIP")
