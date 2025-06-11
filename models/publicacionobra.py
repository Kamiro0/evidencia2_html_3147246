from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class PublicacionObra(Base):
    __tablename__ = "publicaciones_obra"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)
    estado = Column(String(50)) 
    archivo_url = Column(String(255), nullable=False)
    fecha_publicacion = Column(DateTime)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    autor = relationship("Usuario", back_populates="publicaciones_obra")