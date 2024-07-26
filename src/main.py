from fastapi import FastAPI
from dotenv import load_dotenv          #Pour récupérer les infos stockées dans le fichier .env
from src.routes import CRUD_note_route, CRUD_eleve_route, question_projet_route

load_dotenv()       #pour utiliser la fonction et pouvoir utiliser le .env
app = FastAPI()
app.include_router(CRUD_note_route.router)          # Le routeur principal src vient inclure le routeur secondaire CRUD_note_route.router
app.include_router(question_projet_route.router)
app.include_router(CRUD_eleve_route.router)
