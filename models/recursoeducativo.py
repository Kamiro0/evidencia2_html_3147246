from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text

class RecursoEducativo(Base):
    __tablename__ = "recursos_educativos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    archivo = Column(String(255))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
