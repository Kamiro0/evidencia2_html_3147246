from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class LikeObra(Base):
    __tablename__ = "likes_obra"
    id = Column(Integer, primary_key=True)
    publicacion_id = Column(Integer, ForeignKey("publicaciones_obra.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)