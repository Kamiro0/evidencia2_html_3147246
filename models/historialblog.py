from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class HistorialBlog(Base):
    __tablename__ = "historial_blog"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    publicacion_blog_id = Column(Integer, ForeignKey("publicaciones_blog.id"))
    tipo_interaccion = Column(String(50))  
    fecha = Column(DateTime)