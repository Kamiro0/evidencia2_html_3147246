from db import Base
from sqlalchemy import Enum, Column, Integer, String, ForeignKey, Text
from models.enums import TipoArchivoRecurso
class RecursoEducativo(Base):
    __tablename__ = "recursos_educativos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    tipo_archivo = Column(Enum(TipoArchivoRecurso))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    