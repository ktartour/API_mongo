from fastapi import FastAPI
#from pydantic import BaseModel
import os                               #Récup des infos en dehors de nos fichiers python
from dotenv import load_dotenv          #Pour récupérer les infos stockées dans le fichier .env
from urllib.parse import quote_plus     #Encoder les caractères spéciaux (avec les %)
from routes import CRUD_note_route

load_dotenv()       #pour utiliser la fonction et pouvoir utiliser le .env
app = FastAPI()
app.include_router(CRUD_note_route.router)          # Le routeur principal app vient inclure le routeur secondaire CRUD_note_route.router

"""
###             Prof            ###
@app.get("/professeurs/", tags=["Professeur"])
async def get_prof():
    # renvoyer nos données
    return {"L'ensemble des professeurs est":mongo_client.list_prof()}

###         Eleve               ###
@app.get("/eleves/", tags=["Eleves"])
async def get_eleve_par_classe():
    return {"L'ensemble des élèves dans chaque classe est": mongo_client.list_eleve_par_class()}

@app.get("/eleves_par_classe/", tags=["Eleves"])
async def get_eleve_choix_classe(classe):
    return {f"L'ensemble des élèves de {classe} est: {mongo_client.list_eleve_choix_class(classe)}"}

@app.get("/notes par eleve/", tags=["Eleves"])
async def get_note_eleve(prenom,nom):
    return {f"note eleve {mongo_client.note_choix_eleve(prenom,nom)}"}

@app.get("/notes par prof/", tags=["Professeur"])
async def get_note_prof(prenom,nom):
    return {f"Les élèves de {prenom} {nom} ont eu les notes {mongo_client.note_choix_prof(prenom,nom)}"}
"""
"""@app.post("/eleves", tags=["Eleves"])
async def post_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement):
    return mongo_client.fill_notes(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement)

@app.delete("/eleve",tags=["Eleves"])
async def delete_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere):
    return mongo_client.delete_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere)"""