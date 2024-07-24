from fastapi import FastAPI
#from pydantic import BaseModel
import os                               #Récup des infos en dehors de nos fichiers python
from dotenv import load_dotenv          #Pour récupérer les infos stockées dans le fichier .env
from urllib.parse import quote_plus     #Encoder les caractères spéciaux (avec les %)
from routes import CRUD_note_route, question_projet_route, CRUD_eleve_route

load_dotenv()       #pour utiliser la fonction et pouvoir utiliser le .env
app = FastAPI()
app.include_router(CRUD_note_route.router)          # Le routeur principal app vient inclure le routeur secondaire CRUD_note_route.router
app.include_router(question_projet_route.router)
app.include_router(CRUD_eleve_route.router)
