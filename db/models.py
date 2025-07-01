from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DateTime, Date
from sqlalchemy.orm import relationship
class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date)
    tipo_arte_preferido = Column(String(100))
    telefono = Column(String(50), nullable=False)

    registro_actividad = relationship("RegistroActividad", back_populates="usuario")
    configuraciones = relationship("ConfiguracionUsuario", back_populates="usuario", uselist=False)
    notificaciones = relationship("Notificacion", back_populates="usuario")
    mensajes_enviados = relationship("MensajePrivado", foreign_keys='MensajePrivado.id_emisor', back_populates="emisor")
    mensajes_recibidos = relationship("MensajePrivado", foreign_keys='MensajePrivado.id_receptor', back_populates="receptor")
    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    preferencias_arte = relationship("PreferenciaArte", back_populates="usuario")
    seguidores = relationship("SeguidorUsuario", foreign_keys='SeguidorUsuario.id_usuario', back_populates="usuario")
    seguidos = relationship("SeguidorUsuario", foreign_keys='SeguidorUsuario.id_seguidor', back_populates="seguidor")
    publicaciones_obra = relationship("PublicacionObra", back_populates="autor")
    comunidades = relationship("Comunidad", back_populates="administrador")
    publicaciones_comunidad = relationship("PublicacionComunidad", back_populates="autor")
    comentarios_comunidad = relationship("ComentarioComunidad", back_populates="usuario")
    bloqueos = relationship("UsuarioBloqueado", foreign_keys='UsuarioBloqueado.id_usuario', back_populates="usuario")
    bloqueados = relationship("UsuarioBloqueado", foreign_keys='UsuarioBloqueado.id_bloqueado', back_populates="bloqueado")
    verificacion = relationship("Verificacion2Pasos", back_populates="usuario", uselist=False)


class RegistroActividad(Base):
    __tablename__ = "registro_actividad"
    id_actividad = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    accion = Column(String(255))
    fecha = Column(DateTime)
    usuario = relationship("Usuario", back_populates="registro_actividad")


class ConfiguracionUsuario(Base):
    __tablename__ = "configuraciones_usuario"
    id_configuracion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    modo_oscuro = Column(Boolean, default=False)
    idioma_preferido = Column(String(50))
    recibir_notificaciones = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="configuraciones")


class Notificacion(Base):
    __tablename__ = "notificaciones"
    id_notificacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    mensaje = Column(Text)
    leido = Column(Boolean, default=False)
    fecha = Column(DateTime)
    usuario = relationship("Usuario", back_populates="notificaciones")


class MensajePrivado(Base):
    __tablename__ = "mensajes_privados"
    id_mensaje = Column(Integer, primary_key=True)
    id_emisor = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_receptor = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    contenido = Column(Text)
    fecha_envio = Column(DateTime)
    leido = Column(Boolean, default=False)
    emisor = relationship("Usuario", foreign_keys=[id_emisor], back_populates="mensajes_enviados")
    receptor = relationship("Usuario", foreign_keys=[id_receptor], back_populates="mensajes_recibidos")


class Perfil(Base):
    __tablename__ = "perfiles"
    id_perfil = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    descripcion = Column(Text)
    foto_perfil = Column(String(255))
    biografia = Column(Text)
    usuario = relationship("Usuario", back_populates="perfil")


class PreferenciaArte(Base):
    __tablename__ = "preferencias_arte"
    id_preferencia = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    categoria = Column(String(100))
    usuario = relationship("Usuario", back_populates="preferencias_arte")


class SeguidorUsuario(Base):
    __tablename__ = "seguidores_usuario"
    id_seguimiento = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_seguidor = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha_seguimiento = Column(DateTime)
    usuario = relationship("Usuario", foreign_keys=[id_usuario], back_populates="seguidores")
    seguidor = relationship("Usuario", foreign_keys=[id_seguidor], back_populates="seguidos")


class SeguimientoUsuario(Base):
    __tablename__ = "seguimiento_usuario"
    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    accion = Column(String(255))
    detalle = Column(Text)
    fecha = Column(DateTime)
    usuario = relationship("Usuario")


class CategoriaObra(Base):
    __tablename__ = "categorias_obra"
    id_categoria = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text)


class PublicacionObra(Base):
    __tablename__ = "publicaciones_obra"
    id_publicacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias_obra.id_categoria"), nullable=False)
    titulo = Column(String(200), nullable=False)
    descripcion = Column(Text)
    contenido = Column(Text)
    fecha_publicacion = Column(DateTime)
    autor = relationship("Usuario", back_populates="publicaciones_obra")
    categoria = relationship("CategoriaObra")


class LikeObra(Base):
    __tablename__ = "likes_obra"
    id_like = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_obra.id_publicacion"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    tipo_reaccion = Column(String(20))
    fecha_like = Column(DateTime)


class ComentarioObra(Base):
    __tablename__ = "comentarios_obra"
    id_comentario = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_obra.id_publicacion"), nullable=False)
    contenido = Column(Text, nullable=False)
    fecha_comentario = Column(DateTime)
    id_comentario_padre = Column(Integer, ForeignKey("comentarios_obra.id_comentario"), nullable=True)
    es_editado = Column(Boolean, default=False)
    numero_reportes = Column(Integer, default=0)

    usuario = relationship("Usuario")
    publicacion = relationship("PublicacionObra")
    comentario_padre = relationship("ComentarioObra", remote_side=[id_comentario])


class HistorialInteraccionesObra(Base):
    __tablename__ = "historial_interacciones_obra"
    id_historial = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_obra.id_publicacion"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    accion = Column(String(255))
    fecha_accion = Column(DateTime)


class ColeccionArte(Base):
    __tablename__ = "colecciones_arte"
    id_coleccion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    nombre = Column(String(100))
    descripcion = Column(Text)
    fecha_creacion = Column(DateTime)


class ColeccionObra(Base):
    __tablename__ = "colecciones_obras"
    id = Column(Integer, primary_key=True)
    id_coleccion = Column(Integer, ForeignKey("colecciones_arte.id_coleccion"), nullable=False)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_obra.id_publicacion"), nullable=False)


class Comunidad(Base):
    __tablename__ = "comunidades"
    id_comunidad = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    fecha_creacion = Column(DateTime)
    id_administrador = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)

    administrador = relationship("Usuario", back_populates="comunidades")
    publicaciones = relationship("PublicacionComunidad", back_populates="comunidad")


class PublicacionComunidad(Base):
    __tablename__ = "publicaciones_comunidad"
    id_publicacion = Column(Integer, primary_key=True)
    id_comunidad = Column(Integer, ForeignKey("comunidades.id_comunidad"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    contenido = Column(Text)
    fecha_publicacion = Column(DateTime)

    comunidad = relationship("Comunidad", back_populates="publicaciones")
    autor = relationship("Usuario", back_populates="publicaciones_comunidad")


class ComentarioComunidad(Base):
    __tablename__ = "comentarios_comunidad"
    id_comentario = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_comunidad.id_publicacion"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    contenido = Column(Text)
    fecha_comentario = Column(DateTime)

    usuario = relationship("Usuario", back_populates="comentarios_comunidad")


class LikeComunidad(Base):
    __tablename__ = "likes_comunidad"
    id_like = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_comunidad.id_publicacion"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    tipo_reaccion = Column(String(20))
    fecha_like = Column(DateTime)


class HistorialComunidad(Base):
    __tablename__ = "historial_comunidad"
    id_historial = Column(Integer, primary_key=True)
    id_comunidad = Column(Integer, ForeignKey("comunidades.id_comunidad"), nullable=False)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    accion = Column(String(255))
    fecha_accion = Column(DateTime)


class ReporteContenido(Base):
    __tablename__ = "reportes_contenido"
    id_reporte = Column(Integer, primary_key=True)
    id_usuario_reportado = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_usuario_reportante = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    tipo_contenido = Column(String(50))
    id_contenido = Column(Integer)
    motivo = Column(Text)
    evidencia = Column(Text)
    fecha_reporte = Column(DateTime)


class UsuarioBloqueado(Base):
    __tablename__ = "usuarios_bloqueados"
    id_bloqueo = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_bloqueado = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha_bloqueo = Column(DateTime)
    usuario = relationship("Usuario", foreign_keys=[id_usuario], back_populates="bloqueos")
    bloqueado = relationship("Usuario", foreign_keys=[id_bloqueado], back_populates="bloqueados")


class Verificacion2Pasos(Base):
    __tablename__ = "verificacion_2pasos"
    id_verificacion = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    codigo = Column(String(10))
    expiracion = Column(DateTime)
    verificado = Column(Boolean, default=False)
    usuario = relationship("Usuario", back_populates="verificacion")


class GaleriaArte(Base):
    __tablename__ = "galeria_arte"
    id_galeria = Column(Integer, primary_key=True)
    id_publicacion = Column(Integer, ForeignKey("publicaciones_obra.id_publicacion"), nullable=False)
    fecha_agregado = Column(DateTime)