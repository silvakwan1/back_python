from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles  # Correção: Importar StaticFiles corretamente
from app.routes import create_promotion,viw_promotion_location, viw_promotion
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens para desenvolvimento
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Monte o diretório de uploads para servir os arquivos de imagem
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")  # Correção: Usar StaticFiles com 'S' maiúsculo

# Incluir o roteador de promoções
app.include_router(create_promotion.router)
app.include_router(viw_promotion_location.router)
app.include_router(viw_promotion.router)

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API MongoDB com FastAPI"}
