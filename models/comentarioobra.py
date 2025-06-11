from db import Base
from sqlalchemy import Column, Integer, Text, ForeignKey

class ComentarioObra(Base):
    __tablename__ = "comentarios_obra"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    obra_id = Column(Integer, ForeignKey("publicaciones_obra.id"))