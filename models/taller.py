from db import Base
from sqlalchemy import Column, Integer, String, Text, DateTime

class Taller(Base):
    __tablename__ = "talleres"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    fecha_publicacion = Column(DateTime)
    publicaciones_progreso = Column(Text)
    comentarios = Column(Text)
