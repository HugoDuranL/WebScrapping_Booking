from pydantic import BaseModel
from typing import List
from datetime import date

class Reserva(BaseModel):
    destino: str
    data_inicio: date
    data_fim: date
    quantidade_adultos: int
    quantidade_criancas: int
    idade_criancas: List[int]
    quantidade_quartos: int