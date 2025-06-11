from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class LikeComunidad(Base):
    __tablename__ = "likes_comunidad"
    id = Column(Integer, primary_key=True)
    publicacion_comunidad_id = Column(Integer, ForeignKey("publicaciones_comunidad.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)