from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(40), unique=True, nullable=False)
    correo = Column(String(100), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    genero = Column(String(20))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))
    fecha_registro = Column(DateTime)
    perfil = relationship("Perfil", back_populates="usuario", uselist=False)
    publicaciones_obra = relationship("PublicacionObra", back_populates="autor")
    categorias_obra = relationship("CategoriaObra", back_populates="usuario")
    blogs = relationship("Blog", back_populates="administrador")
    publicaciones_blog = relationship("PublicacionBlog", back_populates="autor")
    comunidades = relationship("Comunidad", back_populates="administrador")


class Perfil(Base):
    __tablename__ = "perfiles"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True)
    nombre_completo = Column(String(100))
    biografia = Column(Text)
    foto_perfil = Column(String(255))
    sitio_web = Column(String(255))
    coleccion_arte = Column(Text)  
    talleres_inscritos = Column(Text) 
    amigos = Column(Text)  
    fecha_publicacion = Column(DateTime)
    usuario = relationship("Usuario", back_populates="perfil")


class PublicacionObra(Base):
    __tablename__ = "publicaciones_obra"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)
    estado = Column(String(50)) 
    archivo_url = Column(String(255), nullable=False)
    fecha_publicacion = Column(DateTime)
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    autor = relationship("Usuario", back_populates="publicaciones_obra")


class CategoriaObra(Base):
    __tablename__ = "categorias_obra"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", back_populates="categorias_obra")


class ComentarioObra(Base):
    __tablename__ = "comentarios_obra"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    obra_id = Column(Integer, ForeignKey("publicaciones_obra.id"))


class LikeObra(Base):
    __tablename__ = "likes_obra"
    id = Column(Integer, primary_key=True)
    publicacion_id = Column(Integer, ForeignKey("publicaciones_obra.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)


class HistorialInteracciones(Base):
    __tablename__ = "historial_interacciones"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String(50))  
    referencia_id = Column(Integer) 
    fecha = Column(DateTime)


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    administrador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descripcion = Column(Text)
    fecha_publicacion = Column(DateTime)
    administrador = relationship("Usuario", back_populates="blogs")


class PublicacionBlog(Base):
    __tablename__ = "publicaciones_blog"
    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    contenido = Column(Text, nullable=False)
    fecha_publicacion = Column(DateTime)
    autor = relationship("Usuario", back_populates="publicaciones_blog")


class LikeBlog(Base):
    __tablename__ = "likes_blog"
    id = Column(Integer, primary_key=True)
    publicacion_blog_id = Column(Integer, ForeignKey("publicaciones_blog.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)


class HistorialBlog(Base):
    __tablename__ = "historial_blog"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    publicacion_blog_id = Column(Integer, ForeignKey("publicaciones_blog.id"))
    tipo_interaccion = Column(String(50))  
    fecha = Column(DateTime)


class Comunidad(Base):
    __tablename__ = "comunidades"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    administrador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    descripcion = Column(Text)
    fecha_publicacion = Column(DateTime)
    administrador = relationship("Usuario", back_populates="comunidades")


class MiembroComunidad(Base):
    __tablename__ = "miembros_comunidad"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))


class PublicacionComunidad(Base):
    __tablename__ = "publicaciones_comunidad"
    id = Column(Integer, primary_key=True)
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))
    contenido = Column(Text)
    fecha_publicacion = Column(DateTime)


class LikeComunidad(Base):
    __tablename__ = "likes_comunidad"
    id = Column(Integer, primary_key=True)
    publicacion_comunidad_id = Column(Integer, ForeignKey("publicaciones_comunidad.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo_reaccion = Column(String(50)) 
    fecha_like = Column(DateTime)


class HistorialComunidad(Base):
    __tablename__ = "historial_comunidad"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    publicacion_comunidad_id = Column(Integer, ForeignKey("publicaciones_comunidad.id"))
    tipo_interaccion = Column(String(50)) 
    fecha = Column(DateTime)


class MensajePrivado(Base):
    __tablename__ = "mensajes_privados"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    emisor_id = Column(Integer, ForeignKey("usuarios.id"))
    receptor_id = Column(Integer, ForeignKey("usuarios.id"))


class Notificacion(Base):
    __tablename__ = "notificaciones"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


class Taller(Base):
    __tablename__ = "talleres"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text)
    fecha_inicio = Column(DateTime)
    fecha_fin = Column(DateTime)
    fecha_publicacion = Column(DateTime)
    publicaciones_progreso = Column(Text)
    comentarios = Column(Text)


class InscripcionTaller(Base):
    __tablename__ = "inscripciones_taller"
    id = Column(Integer, primary_key=True)
    taller_id = Column(Integer, ForeignKey("talleres.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    contraseña = Column(String(100))
    fecha_inscripcion = Column(DateTime)


class RecursoEducativo(Base):
    __tablename__ = "recursos_educativos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    archivo = Column(String(255))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))


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


class SeguimientoUsuario(Base):
    __tablename__ = "seguimientos_usuario"
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))