from db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime

class PublicacionComunidad(Base):
    __tablename__ = "publicaciones_comunidad"
    id = Column(Integer, primary_key=True)
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    contenido = Column(Text)
    fecha_publicacion = Column(DateTime)
