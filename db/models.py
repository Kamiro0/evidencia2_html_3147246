from .database import Base
from sqlalchemy import Column, Integer, String


#crear la calse de modelo (identidad)
class Categoria(Base):
    __tablename__= "categorias"
    id = Column(Integer,
                primary_key=True
                )
    nombre = Column(String(50))