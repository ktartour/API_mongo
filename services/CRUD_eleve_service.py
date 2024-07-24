from db import mongo_db


mongo_collection =mongo_db["eleve"]      #Definition de la collection à utiliser


def get_eleve(nom_eleve, prenom_eleve):
    try:

        document = {"nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve}
        eleve= list(mongo_collection.find(document, {"_id": 0}))

        return eleve
    except Exception as e:
        print(f"document non supprimé du à: {e}")


def fill_eleve(nom_eleve, prenom_eleve,nom_classe,date_naissance_eleve,adresse_eleve,sexe_eleve):
    try:
        document = {"nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve,
                    "nom_classe": nom_classe,"date_naissance_eleve": date_naissance_eleve,"adresse_eleve":adresse_eleve,"sexe_eleve":sexe_eleve}
        mongo_collection.insert_one(document)       #Insert le dictionnaire défini dans document
        return "documents insérés"
    except Exception as e:
        print(f"document non inséré du à: {e}")

def modify_eleve_adresse(nom_eleve, prenom_eleve,new_adresse_eleve):
    try:
        document = {"nom_eleve":nom_eleve,"prenom_eleve": prenom_eleve}
        mongo_collection.update_one(document,{"$set" :{"adresse_eleve":new_adresse_eleve}})
        return "document modifié"
    except Exception as e:
        print(f"document non modifié du à: {e}")


def delete_eleve(nom_eleve, prenom_eleve):
    try:

        document = {"nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve}
        mongo_collection.delete_one(document)           #Supprime le document respectant les valeurs définies dans document
        return "document delete"
    except Exception as e:
        print(f"document non supprimé du à: {e}")