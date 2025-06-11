from enum import Enum

class TipoNotificacion(Enum):
    MENSAJE = "Mensaje"
    ALERTA = "Alerta"
    SEGUIDOR_NUEVO = "Seguidor nuevo"
    LIKE = "Like"
    COMENTARIO = "Comentario"
