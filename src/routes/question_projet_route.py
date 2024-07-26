from src.services.question_projet_service import  list_prof, list_eleves, list_eleve_par_class, note_choix_eleve, note_choix_prof
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser

router=APIRouter()


@router.get("/professeurs/", tags=["Professeurs"])
async def obtenir_liste_profs():
    # renvoyer nos données
    return list_prof()


@router.get("/all_eleves/", tags=["Eleves"])
async def obtenir_tous_eleves():
    return list_eleves()


###
@router.get("/eleves_par_classe/", tags=["Eleves"])
async def obtenir_eleves_par_classe(classe):
    return list_eleve_par_class(classe)

@router.get("/notes_par_eleve/", tags=["Eleves"])
async def obtenir_notes_eleve(nom,prenom):
    return note_choix_eleve(prenom,nom)

@router.get("/notes/", tags=["Professeurs"])
async def obtenir_notes_par_prof(nom,prenom):
    return note_choix_prof(prenom,nom)