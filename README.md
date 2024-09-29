# TAREA-02

Esta es una aplicación web sencilla desarrollada con Flask que permite a los usuarios crear, editar y eliminar publicaciones de blog. Además, los usuarios pueden añadir comentarios a las publicaciones sin necesidad de autenticarse. El proyecto incluye funcionalidades de autenticación y edición enriquecida para los posts;
cuyo fin es obtener un puntaje alto en el curso de API DEVELOPER de Cybertec.

## Características

- **Publicaciones de Blog**: Crear, editar y eliminar publicaciones.
- **Comentarios**: Añadir comentarios a las publicaciones sin necesidad de estar registrado.
- **Autenticación**: Iniciar sesión y cerrar sesión para usuarios registrados.
- **Editor de Texto**: Utiliza CKEditor para crear publicaciones con contenido enriquecido.
- **Carga de Imágenes**: Los usuarios pueden cargar una foto de perfil.

## Tecnologías Utilizadas

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy** (manejo de la base de datos)
- **Flask-WTF** (formularios)
- **Flask-Login** (gestión de autenticación)
- **CKEditor** (editor de texto enriquecido)

## USO

Uso
Crear un Usuario

Para crear publicaciones, primero necesitas un usuario. Puedes crear uno accediendo al intérprete de Python y ejecutando lo siguiente:

Abrir el Terminal de Python:

```
python
```

Ejecutar los Siguientes Comandos:
```
from app import create_app
from extensions import db, bcrypt
from models import User

app = create_app()

with app.app_context():
    hashed_password = bcrypt.generate_password_hash('password123').decode('utf-8')
    user = User(username='admin', email='admin@example.com', password=hashed_password)
    db.session.add(user)
    db.session.commit()
```

Este comando creará un usuario con:

    Email: admin@example.com
    Contraseña: password123

Navegar por la Aplicación:
    Página login: Permite acceder con credenciales al blog 
    Página Principal: Muestra todas las publicaciones creadas.
    Crear una Nueva Publicación: Debes estar autenticado para ver el enlace para crear una nueva publicación.
    Añadir Comentarios: Cualquier usuario puede añadir comentarios a las publicaciones.
```
http://127.0.0.1:5000/login
```

Licencia :
Este proyecto está licenciado bajo la Licencia MIT.

Autor :
Creado por Waldo Anthony Berrocal García.
