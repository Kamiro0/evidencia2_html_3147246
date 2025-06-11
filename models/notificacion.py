from db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text

class Notificacion(Base):
    __tablename__ = "notificaciones"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


