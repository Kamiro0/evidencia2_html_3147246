from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class InscripcionTaller(Base):
    __tablename__ = "inscripciones_taller"
    id = Column(Integer, primary_key=True)
    taller_id = Column(Integer, ForeignKey("talleres.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    contraseña = Column(String(100))
    fecha_inscripcion = Column(DateTime)
