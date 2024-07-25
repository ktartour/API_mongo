from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class NoteCreateSchema(BaseModel):
    date_saisie : date
    nom_eleve: str
    prenom_eleve: str
    nom_classe: Optional[str] = None
    nom_matiere: Optional[str] = None
    nom_prof: Optional[str] = None
    prenom_prof: Optional[str] = None
    nom_trimestre: Optional[str] = None
    note: int
    avis: Optional[str] = None
    avancement: Optional[int] = None

class NoteGetSchema(BaseModel):
    date_saisie: date
    nom_eleve: str
    prenom_eleve: str
    nom_classe: Optional[str] = None
    nom_matiere: Optional[str] = None

