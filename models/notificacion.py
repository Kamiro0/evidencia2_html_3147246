from db import Base
from sqlalchemy import Enum, Column, Integer, ForeignKey, Text
from models.enums import TipoNotificacion
class Notificacion(Base):
    __tablename__ = "notificaciones"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(Enum(TipoNotificacion))

