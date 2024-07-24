from services.CRUD_eleve_service import fill_eleve, delete_eleve, get_eleve, modify_eleve_adresse
from fastapi import APIRouter               # Pour pouvoir utiliser des routeurs secondaires = des routers definis dans des sous dossiers et appelés dans le main pour les utiliser

router=APIRouter(tags=["Eleves"])          #defini le routeur pour cette page, prédéfini le tag pour toutes les fonctions de cette page: Eleves

@router.post("/Eleves")
async def post_eleve(nom_eleve,prenom_eleve):
    return fill_eleve(nom_eleve,prenom_eleve)
@router.get("/Eleves")
async def get_eleve(nom_eleve, prenom_eleve,nom_classe,date_naissance_eleve,adresse_eleve,sexe_eleve):
    return get_eleve(nom_eleve, prenom_eleve,nom_classe,date_naissance_eleve,adresse_eleve,sexe_eleve)

@router.patch("/Eleves")
async def update(nom_eleve, prenom_eleve,new_adresse_eleve):
    return modify_eleve_adresse(nom_eleve, prenom_eleve,new_adresse_eleve)


@router.delete("/Eleves")
async def delete_eleve(nom_eleve,prenom_eleve):
    return delete_eleve(nom_eleve,prenom_eleve)