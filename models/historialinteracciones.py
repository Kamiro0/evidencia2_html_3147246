from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

class HistorialInteracciones(Base):
    __tablename__ = "historial_interacciones"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String(50))  
    referencia_id = Column(Integer) 
    fecha = Column(DateTime)
