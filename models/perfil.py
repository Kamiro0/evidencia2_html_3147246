from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class Perfil(Base):
    __tablename__ = "perfiles"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True)
    nombre_completo = Column(String(100))
    biografia = Column(Text)
    foto_perfil = Column(String(255))
    sitio_web = Column(String(255))
    coleccion_arte = Column(Text)  
    talleres_inscritos = Column(Text) 
    amigos = Column(Text)  
    fecha_publicacion = Column(DateTime)
    usuario = relationship("Usuario", back_populates="perfil")
    