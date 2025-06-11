from db import Base
from sqlalchemy import Enum, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.enums import Genero, Categoria
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(40), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    genero = Column(Enum(Genero))
    categoria = Column(Enum(Categoria), nullable=False)
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))
    fecha_registro = Column(DateTime)
    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    publicaciones_obra = relationship("PublicacionObra", back_populates="autor")
    categorias_obra = relationship("CategoriaObra", back_populates="usuario")
    blogs = relationship("Blog", back_populates="administrador")
    publicaciones_blog = relationship("PublicacionBlog", back_populates="autor")
    comunidades = relationship("Comunidad", back_populates="administrador")