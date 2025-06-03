from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
#crear la calse de modelo (identidad)
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre_usuario = Column(String(40), unique=True)
    correo = Column(String(100), unique=True)
    contraseña = Column(String(255))
    nombre_completo = Column(String(100))


class Perfil(Base):
    __tablename__ = "perfiles"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    biografia = Column(Text)
    foto_perfil = Column(String(255))


class ObraArte(Base):
    __tablename__ = "obras_arte"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    archivo = Column(String(255))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    categoria_id = Column(Integer, ForeignKey("categorias_obra.id"))


class CategoriaObra(Base):
    __tablename__ = "categorias_obra"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))


class ComentarioObra(Base):
    __tablename__ = "comentarios_obra"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    obra_id = Column(Integer, ForeignKey("obras_arte.id"))


class LikeObra(Base):
    __tablename__ = "likes_obra"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    obra_id = Column(Integer, ForeignKey("obras_arte.id"))


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


class ComentarioBlog(Base):
    __tablename__ = "comentarios_blog"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))


class Comunidad(Base):
    __tablename__ = "comunidades"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    descripcion = Column(Text)
    creador_id = Column(Integer, ForeignKey("usuarios.id"))


class MiembroComunidad(Base):
    __tablename__ = "miembros_comunidad"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))


class PublicacionComunidad(Base):
    __tablename__ = "publicaciones_comunidad"
    id = Column(Integer, primary_key=True)
    contenido = Column(Text)
    comunidad_id = Column(Integer, ForeignKey("comunidades.id"))
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


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
    nombre = Column(String(100))
    descripcion = Column(Text)
    cupo = Column(Integer)
    creador_id = Column(Integer, ForeignKey("usuarios.id"))


class InscripcionTaller(Base):
    __tablename__ = "inscripciones_taller"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    taller_id = Column(Integer, ForeignKey("talleres.id"))


class RecursoEducativo(Base):
    __tablename__ = "recursos_educativos"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    descripcion = Column(Text)
    archivo = Column(String(255))
    autor_id = Column(Integer, ForeignKey("usuarios.id"))


class HistorialInteracciones(Base):
    __tablename__ = "historial_interacciones"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    tipo = Column(String(50)) 
    referencia_id = Column(Integer) 


class ReportePlagio(Base):
    __tablename__ = "reportes_plagio"
    id = Column(Integer, primary_key=True)
    obra_id = Column(Integer, ForeignKey("obras_arte.id"))
    reportado_por_id = Column(Integer, ForeignKey("usuarios.id"))
    descripcion = Column(Text)


class ConfiguracionUsuario(Base):
    __tablename__ = "configuraciones_usuario"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))


class SeguimientoUsuario(Base):
    __tablename__ = "seguimientos_usuario"
    id = Column(Integer, primary_key=True)
    seguidor_id = Column(Integer, ForeignKey("usuarios.id"))
    seguido_id = Column(Integer, ForeignKey("usuarios.id"))

   
    

    
