import os                               #Récup des infos en dehors de nos fichiers python
from dotenv import load_dotenv          #Pour récupérer les infos stockées dans le fichier .env
from urllib.parse import quote_plus     #Encoder les caractères spéciaux (avec les %)
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from motor import motor_asyncio     #Pour essayer de faire fonctionner la fonction async en remplaçant MongoClient

load_dotenv()       #pour utiliser la fonction et pouvoir utiliser le .env

datab_name = os.environ["DB_NAME"]
utilisateur = os.environ["Nom_utilisateur"]
mdp = os.environ["MDP"]
cluster = os.environ["CLUSTER"]


mdp2 = quote_plus(mdp)              #pour recoder en cas de caractères spéciaux

URI="mongodb+srv://"+utilisateur+":"+mdp2+"@"+cluster+".mongodb.net/"       #Reconstitution de l'URI

mongo_client=MongoClient(URI, server_api=ServerApi ("1"), tls=True)
mongo_db=mongo_client[datab_name]


try:
    ping = mongo_client.admin.command({'ping': 1})
    print(f"Pinged your deployment: {ping}. You successfully connected to MongoDB!")
except Exception as e:
    raise Exception("Unable to connect to MongoDB due to the following")