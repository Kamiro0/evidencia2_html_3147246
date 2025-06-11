from db import Base
from sqlalchemy import Column, Integer, ForeignKey

class SeguimientoUsuario(Base):
    __tablename__ = "seguimientos_usuario"
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))