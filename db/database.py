from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
Base = declarative_base()
#Variable cadena de conexion:
MARIADB_URL="mysql+pymysql://root:admin@localhost:3315/pyshop-3147246"
#Crear el objeto conexion de la base de datos
engine = create_engine(MARIADB_URL)