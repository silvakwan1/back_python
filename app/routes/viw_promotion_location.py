from fastapi import APIRouter, HTTPException, Query
from app.database import cursor  # Supondo que você tenha o cursor configurado no database.py
from math import radians, sin, cos, sqrt, atan2
from decimal import Decimal
from datetime import datetime, date
import os
from app.func.delete import deletar_promocoes_expiradas

router = APIRouter()

# Constante para o raio da Terra em quilômetros
EARTH_RADIUS_KM = 6371
UPLOAD_FOLDER = "uploads"  # Diretório onde as imagens estão armazenadas

def calculate_distance(lat1, lon1, lat2, lon2):
    """Calcula a distância entre dois pontos geográficos."""
    d_lat = radians(lat2 - lat1)
    d_lon = radians(lon2 - lon1)
    a = (
        sin(d_lat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(d_lon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return EARTH_RADIUS_KM * c


@router.get('/promotions/location')
async def get_promotions_sorted_by_distance(
    latitude: float = Query(..., description="Latitude do usuário"),
    longitude: float = Query(..., description="Longitude do usuário"),
    radius: float = Query(20.0, description="Raio em quilômetros")
):
    try:
        # Primeiro, deletamos as promoções expiradas
        deletar_promocoes_expiradas()

        # Em seguida, pegamos as promoções válidas e calculamos a distância
        user_latitude = Decimal(latitude)
        user_longitude = Decimal(longitude)

        cursor.execute("SELECT * FROM Promocoes")
        promotions = cursor.fetchall()

        promotions_with_distance = []
        for promotion in promotions:
            promo_data = {
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
            }

            if promo_data["latitude"] is not None and promo_data["longitude"] is not None:
                promo_latitude = Decimal(promo_data["latitude"])
                promo_longitude = Decimal(promo_data["longitude"])

                distance = calculate_distance(
                    user_latitude, user_longitude,
                    promo_latitude, promo_longitude
                )
                promo_data["distance"] = distance

                # Adiciona promoções dentro do raio especificado
                if distance <= radius:
                    promotions_with_distance.append(promo_data)

                # Caso a promoção tenha coordenadas 0,0, inclui com distância 0
                if promo_latitude == 0 and promo_longitude == 0: 
                    promotions_with_distance.append(promo_data)
                    promo_data["distance"] = 0.0

        # Ordena promoções com base na distância
        promotions_sorted = sorted(promotions_with_distance, key=lambda x: x["distance"])

        return promotions_sorted

    except Exception as e:
        print("Erro ao buscar promoções:", e)
        raise HTTPException(status_code=500, detail="Erro interno ao buscar promoções")
