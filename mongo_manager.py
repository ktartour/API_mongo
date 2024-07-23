from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import  List                                #Pour mettre des contraintes de type
from iteration_utilities import unique_everseen         #Pour dédupliquer un liste

class MongoManager:
    def __init__(self,URI:str, db_name:str, coll_name):                 # :str une info , pas une restriction
        self.__client = MongoClient(URI, server_api=ServerApi ("1"), tls=True)            #tls pour sécurisé le transfert de données, Attribut pour accéder au moteur de la BDD Mongo (ex: compass)
        try:
            ping = self.__client.admin.command({'ping': 1})
            print(f"Pinged your deployment: {ping}. You successfully connected to MongoDB!")
        except Exception as e:
            raise Exception("Unable to connect to MongoDB due to the following"
                            " error: ", e)
        self.__db = self.__client[db_name]               #Attribut pour accéder à la base de données en mode dictionnaire ou self.__db = self.__client.get_database(db_name)
        self.__collection = self.__db[coll_name]        #Attribut pour accéder à la collection aussi possible avec get_collection(coll_name)

    def list_prof(self):
        try:
            liste_de_prof=list(self.__collection.find({}, {"_id": 0, "nom_prof": 1}))
            liste_de_prof = [d['nom_prof'] for d in liste_de_prof]
            return liste_de_prof
        except Exception as e:
            print(e)