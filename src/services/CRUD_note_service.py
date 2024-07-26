from src.config.db import mongo_db
from datetime import datetime

mongo_collection =mongo_db["notes"]      #Definition de la collection à utiliser


def get_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    try:

        document = {"date_saisie": datetime.strptime(date_saisie, "%Y-%m-%d"), "nom_eleve": nom_eleve.lower(), "prenom_eleve": prenom_eleve.lower(),
                    "nom_classe": nom_classe.lower(), "nom_matiere": nom_matiere.lower()}
        note= list(mongo_collection.find(document, {"_id": 0}))

        return note
    except Exception as e:
        print(f"document non supprimé du à: {e}")


def fill_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, nom_prof, prenom_prof,
               nom_trimestre, note, avis, avancement):
    try:
        document = {"date_saisie": datetime.strptime(date_saisie, "%Y-%m-%d"), "nom_eleve": nom_eleve.lower(), "prenom_eleve": prenom_eleve.lower(),
                    "nom_classe": nom_classe.lower(), "nom_matiere": nom_matiere.lower(), "nom_prof": nom_prof.lower(),
                    "prenom_prof": prenom_prof.lower(), "nom_trimestre": nom_trimestre.lower(), "note": int(note), "avis": avis.lower(),
                    "avancement": int(avancement)}
        mongo_collection.insert_one(document)       #Insert le dictionnaire défini dans document
        return "documents insérés"
    except Exception as e:
        print(f"document non inséré du à: {e}")

def fill_notes2(item):
    item= dict(item)
    item["date_saisie"] = datetime.strptime(str(item["date_saisie"]), "%Y-%m-%d")
    item["nom_eleve"] = item["nom_eleve"].lower()
    item["prenom_eleve"] = item["prenom_eleve"].lower()
    item["nom_classe"] = item["nom_classe"].lower()
    item["nom_matiere"] = item["nom_matiere"].lower()
    item["nom_prof"] = item["nom_prof"].lower()
    item["prenom_prof"] = item["prenom_prof"].lower()
    item["note"] = int(item["note"])
    item["nom_trimestre"] = item["nom_trimestre"].lower()
    item["avis"] = item["avis"].lower()
    item["avancement"] = int(item["avancement"])
    try:
        mongo_collection.insert_one(dict(item))       #Insert le dictionnaire défini dans document
        return "documents insérés"
    except Exception as e:
        print(f"document non inséré du à: {e}")

def modify_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note):
    try:
        document = {"date_saisie": datetime.strptime(date_saisie, "%Y-%m-%d"), "nom_eleve": nom_eleve.lower(), "prenom_eleve": prenom_eleve.lower(),
                    "nom_classe": nom_classe.lower(), "nom_matiere": nom_matiere.lower()}
        mongo_collection.update_one(document,{"$set" :{"note" : int(new_note)}})
        return "document modifié"
    except Exception as e:
        print(f"document non modifié du à: {e}")

def modify_notes2(find,item):
    find = dict(find)
    find["date_saisie"] = datetime.strptime(str(find["date_saisie"]), "%Y-%m-%d")
    find["nom_eleve"] = find["nom_eleve"].lower()
    find["prenom_eleve"] = find["prenom_eleve"].lower()
    find["nom_classe"] = find["nom_classe"].lower()
    find["nom_matiere"] = find["nom_matiere"].lower()

    item= dict(item)
    item["date_saisie"] = datetime.strptime(str(item["date_saisie"]), "%Y-%m-%d")
    item["nom_eleve"] = item["nom_eleve"].lower()
    item["prenom_eleve"] = item["prenom_eleve"].lower()
    item["nom_classe"] = item["nom_classe"].lower()
    item["nom_matiere"] = item["nom_matiere"].lower()
    item["nom_prof"] = item["nom_prof"].lower()
    item["prenom_prof"] = item["prenom_prof"].lower()
    item["note"] = int(item["note"])
    item["nom_trimestre"] = item["nom_trimestre"].lower()
    item["avis"] = item["avis"].lower()
    item["avancement"] = int(item["avancement"])
    try:
        mongo_collection.update_one(find, {"$set": item})


        return "document modifié"
    except Exception as e:
        print(f"document non supprimé du à: {e}")
def delete_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    try:

        document = {"date_saisie": datetime.strptime(date_saisie, "%Y-%m-%d"), "nom_eleve": nom_eleve.lower(), "prenom_eleve": prenom_eleve.lower(),
                    "nom_classe": nom_classe.lower(), "nom_matiere": nom_matiere.lower()}
        mongo_collection.delete_one(document)           #Supprime le document respectant les valeurs définies dans document
        return "document delete"
    except Exception as e:
        print(f"document non supprimé du à: {e}")