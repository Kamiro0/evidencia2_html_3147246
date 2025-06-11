from db import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime

class MiembroComunidad(Base):
    __tablename__ = "miembros_comunidad"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))
