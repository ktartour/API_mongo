from services.question_projet_service import  list_prof, list_eleves, list_eleve_par_class, note_choix_eleve, note_choix_prof
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser

router=APIRouter()


@router.get("/Professeurs/", tags=["Professeur"])
async def get_prof():
    # renvoyer nos données
    return {"L'ensemble des professeurs est":list_prof()}


@router.get("/Eleves/", tags=["Eleves"])
async def get_eleves():
    return {"L'ensemble des élèves dans chaque classe est": list_eleves()}


###
@router.get("/Eleves_par_classe/", tags=["Eleves"])
async def get_eleve_par_classe(classe):
    return {f"L'ensemble des élèves de {classe} est: {list_eleve_par_class(classe)}"}

@router.get("/Notes par eleve/", tags=["Eleves"])
async def get_note_eleve(prenom,nom):
    return {f"Les notes de l'eleve {prenom} {nom} sont {note_choix_eleve(prenom,nom)}"}

@router.get("/Notes par prof/", tags=["Professeur"])
async def get_note_prof(prenom,nom):
    return {f"Les élèves du professeur {prenom} {nom} ont eu les notes {note_choix_prof(prenom,nom)}"}