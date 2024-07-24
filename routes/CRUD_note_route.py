from services.CRUD_note_service import fill_notes , delete_note, get_notes, modify_notes
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser

router=APIRouter(tags=["Note"])          #defini le routeur pour cette page, prédéfini le tag pour toutes les fonctions de cette page: Eleves

@router.post("/Nouvelle note")
async def ajout_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement):
    return fill_notes(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere,nom_prof,prenom_prof,nom_trimestre,note,avis,avancement)
@router.get("/Note")
async def obtenir_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    return get_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere)

@router.patch("/Note")
async def mise_a_jour_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note):
    return modify_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note)

@router.delete("/Note")
async def suppression_notes(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere):
    return delete_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere)