from services.CRUD_note_service import fill_notes , fill_notes2, delete_notes, get_notes, modify_notes, modify_notes2
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser
from schemas.note_schema import NoteCreateSchema, NoteGetSchema
from pydantic import BaseModel
from typing import Optional

router=APIRouter(tags=["Note"])          #defini le routeur pour cette page, prédéfini le tag pour toutes les fonctions de cette page: Eleves

@router.get("/note")
async def obtenir_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere):
    return get_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere)


@router.post("/nouvelle_note")
async def ajout_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, nom_prof, prenom_prof,nom_trimestre, note, avis, avancement):
    return fill_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, nom_prof, prenom_prof,nom_trimestre, note, avis, avancement)

@router.post("/nouvelle_note2")
async def ajout_note2(item :NoteCreateSchema):
    return fill_notes2(item)

@router.patch("/note")
async def mise_a_jour_note(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note):
    return modify_notes(date_saisie, nom_eleve, prenom_eleve, nom_classe, nom_matiere, new_note)

@router.patch("/note2")
async def mise_a_jour_note2(find: NoteGetSchema,item: NoteCreateSchema):
    return modify_notes2(find,item)

@router.delete("/note")
async def suppression_note(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere):
    return delete_notes(date_saisie,nom_eleve,prenom_eleve,nom_classe,nom_matiere)