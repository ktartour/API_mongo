from services.CRUD_eleve_service import fill_eleve, delete_eleves, get_eleves, modify_eleve_adresse
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser

router=APIRouter(tags=["Eleves"])          #defini le routeur pour cette page, prédéfini le tag pour toutes les fonctions de cette page: Eleves

@router.post("/Eleves")
async def ajout_eleve(nom_eleve,prenom_eleve,nom_classe,date_naissance_eleve,adresse_eleve,sexe_eleve):
    return fill_eleve(nom_eleve,prenom_eleve,nom_classe,date_naissance_eleve,adresse_eleve,sexe_eleve)

@router.get("/Eleves")
async def obtenir_eleve(nom_eleve, prenom_eleve):
    return get_eleves(nom_eleve, prenom_eleve)

@router.patch("/Adresse eleves")
async def mise_a_jour_adresse(nom_eleve, prenom_eleve,new_adresse_eleve):
    return modify_eleve_adresse(nom_eleve, prenom_eleve,new_adresse_eleve)


@router.delete("/Eleves")
async def suppression_eleve(nom_eleve,prenom_eleve):
    return delete_eleves(nom_eleve,prenom_eleve)