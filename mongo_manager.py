from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#from typing import  List                                #Pour mettre des contraintes de type
#from iteration_utilities import unique_everseen         #Pour dédupliquer un liste
"""  
class MongoManager:
  def __init__(self,URI:str, db_name:str):                 # :str une info , pas une restriction
        self.__client = MongoClient(URI, server_api=ServerApi ("1"), tls=True)            #tls pour sécurisé le transfert de données, Attribut pour accéder au moteur de la BDD Mongo (ex: compass)
        try:
            ping = self.__client.admin.command({'ping': 1})
            print(f"Pinged your deployment: {ping}. You successfully connected to MongoDB!")
        except Exception as e:
            raise Exception("Unable to connect to MongoDB due to the following"
                            " error: ", e)
        self.__db = self.__client[db_name]   """            #Attribut pour accéder à la base de données en mode dictionnaire ou self.__db = self.__client.get_database(db_name)

"""


    def list_prof(self):
        try:
            self.__collection = self.__db["prof"]  # Attribut pour accéder à la collection
            liste_de_prof=list(self.__collection.find({}, {"_id": 0, "nom_prof": 1}))
            liste_de_prof = [d['nom_prof'] for d in liste_de_prof]
            return liste_de_prof
        except Exception as e:
            print(e)

    def list_eleve_par_class(self):
        try:
            self.__collection = self.__db["eleve"]  # Attribut pour accéder à la collection
            liste_eleves = list(self.__collection.find({},{"_id": 0, "nom_eleve": 1, "prenom_eleve": 1, "nom_classe": 1}).sort({"nom_classe":1}))
            liste_eleves = [d['prenom_eleve']+" "+d["nom_eleve"]+" "+d["nom_classe"] for d in liste_eleves]
            return liste_eleves
        except Exception as e:
            print(e)

    def list_eleve_choix_class(self, classe):
        try:
            self.__collection = self.__db["eleve"]  # Attribut pour accéder à la collection
            liste_eleves = list(self.__collection.find({"nom_classe":classe},{"_id": 0, "nom_eleve": 1, "prenom_eleve": 1, "nom_classe": 1}))
            liste_eleves = [d['prenom_eleve']+" "+d["nom_eleve"]+" "+d["nom_classe"] for d in liste_eleves]
            return liste_eleves
        except Exception as e:
            print(e)

    def note_choix_eleve(self, prenom, nom):
        try:
            self.__collection = self.__db["notes"]  # Attribut pour accéder à la collection
            liste_notes = list(self.__collection.find({"nom_eleve":nom,"prenom_eleve":prenom},{
                "_id":0,"prenom_eleve":1,"nom_eleve":1,"nom_matiere":1,"note":1}))
            liste_notes = [d['prenom_eleve']+" "+d["nom_eleve"]+" "+d["nom_matiere"]+" "+str(d["note"]) for d in liste_notes]
            return liste_notes
        except Exception as e:
            print(e)

    def note_choix_prof(self, prenom, nom):
        try:
            self.__collection = self.__db["notes"]  # Attribut pour accéder à la collection
            liste_notes = list(self.__collection.find({"nom_prof":nom,"prenom_prof":prenom},{
                "_id":0,"prenom_eleve":1,"nom_eleve":1,"nom_matiere":1,"note":1}))
            liste_notes = [d['prenom_eleve']+" "+d["nom_eleve"]+" "+d["nom_matiere"]+" "+str(d["note"]) for d in liste_notes]
            return liste_notes
        except Exception as e:
            print(e)
"""
"""    def fill_notes(self,date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement):
        try:
            self.__collection = self.__db["notes"]  # Attribut pour accéder à la collection
            document= {"date_saisie":date_saisie,"nom_eleve":nom_eleve,"prenom_eleve":prenom_eleve,"nom_classe":nom_classe,"nom_matiere":nom_matiere,"nom_prof":nom_prof,"prenom_prof":prenom_prof,"nom_trimestre":nom_trimestre,"note":int(note),"avis":avis,"avancement":int(avancement)}
            self.__collection.insert_one(document)  # possible de faire un return pour savoir commment ça s'est passé
            return "documents insérés"
        except Exception as e:
            print(f"document non inséré du à: {e}")

    def delete_note(self,date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere):
        try:
            self.__collection = self.__db["notes"]  # Attribut pour accéder à la collection
            document = {"date_saisie":date_saisie,"nom_eleve":nom_eleve,"prenom_eleve":prenom_eleve,"nom_classe":nom_classe,"nom_matiere":nom_matiere}
            self.__collection.delete_one(document)
            #delete_result = self.__collection.delete_one({document})
            return "document delete" #{"acknowledged": delete_result.acknowledged, "deletedCount": delete_result.deleted_count}
        except Exception as e:
            print(f"document non supprimé du à: {e}")"""