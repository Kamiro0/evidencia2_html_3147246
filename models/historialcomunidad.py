from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class HistorialComunidad(Base):
    __tablename__ = "historial_comunidad"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    publicacion_comunidad_id = Column(Integer, ForeignKey("publicaciones_comunidad.id"))
    tipo_interaccion = Column(String(50)) 
    fecha = Column(DateTime)