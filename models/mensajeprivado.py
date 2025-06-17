
from db import Base
from sqlalchemy import Enum, Column, Integer, ForeignKey, Text
from models.enums import EstadoMensaje
class MensajePrivado(Base):
    __tablename__ = "mensajes_privados"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    emisor_id = Column(Integer, ForeignKey("usuarios.id"))
    receptor_id = Column(Integer, ForeignKey("usuarios.id"))
    estado = Column(Enum(EstadoMensaje))