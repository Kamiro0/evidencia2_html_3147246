from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class CategoriaObra(Base):
    __tablename__ = "categorias_obra"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="categorias_obra")
