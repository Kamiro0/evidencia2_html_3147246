from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class Comunidad(Base):
    __tablename__ = "comunidades"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    administrador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descripcion = Column(Text)
    fecha_publicacion = Column(DateTime)
    administrador = relationship("Usuario", back_populates="comunidades")