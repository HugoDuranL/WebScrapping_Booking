from fastapi import APIRouter
from model.reserva import Reserva
from webScrapping_Hoteis import teste

router = APIRouter(prefix="/coleta_concorrentes")

@router.post("")
async def coleta_concorrentes(request: Reserva):
    # Lógica para processar a reserva e retornar uma resposta
    response = teste(request)
    resposta = {
        "Mensagem": "Consulta com Sucesso!",
        "Reserva": response
    }
    return resposta
