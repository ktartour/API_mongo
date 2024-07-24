from db import mongo_db


mongo_collection =mongo_db["notes"]      #Definition de la collection à utiliser


def get_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    try:

        document = {"date_saisie": date_saisie, "nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve,
                    "nom_classe": nom_classe, "nom_matiere": nom_matiere}
        note= list(mongo_collection.find(document, {"_id": 0}))

        return note
    except Exception as e:
        print(f"document non supprimé du à: {e}")


def fill_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, nom_prof, prenom_prof,
               nom_trimestre, note, avis, avancement):
    try:
        document = {"date_saisie": date_saisie, "nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve,
                    "nom_classe": nom_classe, "nom_matiere": nom_matiere, "nom_prof": nom_prof,
                    "prenom_prof": prenom_prof, "nom_trimestre": nom_trimestre, "note": int(note), "avis": avis,
                    "avancement": int(avancement)}
        mongo_collection.insert_one(document)       #Insert le dictionnaire défini dans document
        return "documents insérés"
    except Exception as e:
        print(f"document non inséré du à: {e}")

def modify_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note):
    try:
        document = {"date_saisie": date_saisie, "nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve,
                    "nom_classe": nom_classe, "nom_matiere": nom_matiere}       #"note": int(note)
        mongo_collection.update_one(document,{"$set" :{"note" : int(new_note)}})       #Insert le dictionnaire défini dans document
        return "document modifié"
    except Exception as e:
        print(f"document non modifié du à: {e}")


def delete_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    try:

        document = {"date_saisie": date_saisie, "nom_eleve": nom_eleve, "prenom_eleve": prenom_eleve,
                    "nom_classe": nom_classe, "nom_matiere": nom_matiere}
        mongo_collection.delete_one(document)           #Supprime le document respectant les valeurs définies dans document
        return "document delete"
    except Exception as e:
        print(f"document non supprimé du à: {e}")