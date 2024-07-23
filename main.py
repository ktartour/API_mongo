from fastapi import FastAPI
from pydantic import BaseModel
import os                               #Récup des infos en dehors de nos fichiers python
from dotenv import load_dotenv          #Pour récupérer les infos stockées dans le fichier .env
from urllib.parse import quote_plus     #Encoder les caractères spéciaux (avec les %)
from mongo_manager import MongoManager
load_dotenv()       #pour utiliser la fonction et poivoir utiliser le .env
app = FastAPI()

datab_name = os.environ["DB_NAME"]
utilisateur = os.environ["Nom_utilisateur"]
mdp = os.environ["MDP"]
cluster = os.environ["CLUSTER"]


mdp2 = quote_plus(mdp)              #pour recoder en cas de caractères spéciaux

URI="mongodb+srv://"+utilisateur+":"+mdp2+"@"+cluster+".mongodb.net/"       #Reconstitution de l'URI

mongo_client=MongoManager(URI,datab_name)      #Instanciation pour consulter la collection prof

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
    return {"L'ensemble des élèves dans chaque classe est": mongo_client.list_eleve_choix_class(classe)}

@app.get("/notes par eleve/", tags=["Eleves"])
async def get_note_eleve(prenom,nom):
    return {f"note eleve {mongo_client.note_choix_eleve(prenom,nom)}"}

@app.get("/notes par prof/", tags=["Eleves"])
async def get_note_prof(prenom,nom):
    return {f"Les élèves de {prenom} {nom} ont eu les notes {mongo_client.note_choix_prof(prenom,nom)}"}

@app.post("/eleves", tags=["Professeur"])
async def post_lieu(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement):
    return mongo_client.fill_notes(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement)

