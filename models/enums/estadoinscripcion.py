from enum import Enum

class EstadoInscripcion(Enum):
    PENDIENTE = "Pendiente"
    ACEPTADO = "Aceptado"
    RECHAZADO = "Rechazado"
    FINALIZADO = "Finalizado"