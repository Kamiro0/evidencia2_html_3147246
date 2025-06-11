from db import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

class PublicacionBlog(Base):
    __tablename__ = "publicaciones_blog"
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    contenido = Column(Text, nullable=False)
    fecha_publicacion = Column(DateTime)
    autor = relationship("Usuario", back_populates="publicaciones_blog")