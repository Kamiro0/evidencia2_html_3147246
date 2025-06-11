from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class LikeBlog(Base):
    __tablename__ = "likes_blog"
    id = Column(Integer, primary_key=True)
    publicacion_blog_id = Column(Integer, ForeignKey("publicaciones_blog.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)
