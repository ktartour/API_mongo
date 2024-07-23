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

mongo_prof=MongoManager(URI,datab_name,"prof")      #Instanciation pour consulter la collection prof

###             Prof            ###
@app.get("/professeurs/", tags=["Professeur"])
async def get_prof():
    # renvoyer nos données
    return {"L'ensemble des professeurs est":mongo_prof.list_prof()}

###         Eleve               ###
@app.get("/eleves/", tags=["Eleves"])
async def get_eleve_par_classe():
    return {"donnees": mongo_prof.list_prof()}