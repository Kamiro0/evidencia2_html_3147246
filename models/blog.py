from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    administrador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descripcion = Column(Text)
    fecha_publicacion = Column(DateTime)
    administrador = relationship("Usuario", back_populates="blogs")