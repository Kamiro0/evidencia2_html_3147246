from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class ConfiguracionesUsuario(Base):
    __tablename__ = "configuraciones_usuario"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tu_cuenta = Column(String(50))
    accesibilidad_pantalla_idiomas = Column(String(50))
    privacidad_seguridad = Column(String(50))
    centro_ayudas = Column(String(50))
    reporte_usuarios_bloqueados = Column(String(50))
    cerrar_sesion = Column(String(50))