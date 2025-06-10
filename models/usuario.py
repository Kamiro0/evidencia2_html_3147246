from db import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(40), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    genero = Column(String(20))
    fecha_nacimiento = Column(String(50))
    telefono = Column(String(20))
    fecha_registro = Column(String(50))
    