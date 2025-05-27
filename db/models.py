from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


#crear la calse de modelo (identidad)
class Categoria(Base):
    __tablename__= "categorias"
    id = Column(Integer,
                primary_key=True
                )
    nombre = Column(String(50))
class Categoria(Base):
    __tablename__ = "productos"
    nombre = Column(String(40))
    modelo= Column(String(40))
    precio = Column(Integer)
    id = Column(Integer, primary_key=True)
    Categoria_id = Column(Integer,
                        ForeignKey("categorias.id")
                        )
   
    

    
