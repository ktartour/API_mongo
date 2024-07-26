from src.config.db import mongo_db


mongo_collection_prof =mongo_db["prof"]      #Definition de la collection à utiliser
mongo_collection_eleve=mongo_db["eleve"]
mongo_collection_note=mongo_db["notes"]

def list_prof():
    try:
        liste_de_prof = list(mongo_collection_prof.find({}, {"_id": 0, "prenom_prof":1, "nom_prof": 1}))
        liste_de_prof = [d["prenom_prof"]+" "+d['nom_prof'] for d in liste_de_prof]
        return liste_de_prof
    except Exception as e:
        print(e)

def list_eleves():
    try:
        liste_eleves = list(
            mongo_collection_eleve.find({}, {"_id": 0, "nom_eleve": 1, "prenom_eleve": 1, "nom_classe": 1}).sort(
                {"nom_classe": 1}))
        liste_eleves = [d['prenom_eleve'] + " " + d["nom_eleve"] + " " + d["nom_classe"] for d in liste_eleves]
        return liste_eleves
    except Exception as e:
        print(e)


def list_eleve_par_class(classe):
    try:
        liste_eleves = list(mongo_collection_eleve.find({"nom_classe": classe.lower()},
                                                   {"_id": 0, "nom_eleve": 1, "prenom_eleve": 1, "nom_classe": 1}))
        liste_eleves = [d['prenom_eleve'] + " " + d["nom_eleve"] + " " + d["nom_classe"] for d in liste_eleves]
        return liste_eleves
    except Exception as e:
        print(e)


def note_choix_eleve(prenom, nom):
    try:
        liste_notes = list(mongo_collection_note.find({"nom_eleve": nom.lower(), "prenom_eleve": prenom.lower()}, {
            "_id": 0, "prenom_eleve": 1, "nom_eleve": 1, "nom_matiere": 1, "note": 1}))
        liste_notes = [d['prenom_eleve'] + " " + d["nom_eleve"] + " " + d["nom_matiere"] + " " + str(d["note"]) for d in
                       liste_notes]
        return liste_notes
    except Exception as e:
        print(e)


def note_choix_prof(prenom,nom):
    try:
        liste_notes = list(mongo_collection_note.find({"nom_prof": nom.lower(), "prenom_prof": prenom.lower()}, {
            "_id": 0, "prenom_eleve": 1, "nom_eleve": 1, "nom_matiere": 1, "note": 1}))
        liste_notes = [d['prenom_eleve'] + " " + d["nom_eleve"] + " " + d["nom_matiere"] + " " + str(d["note"]) for d in
                       liste_notes]
        return liste_notes
    except Exception as e:
        print(e)