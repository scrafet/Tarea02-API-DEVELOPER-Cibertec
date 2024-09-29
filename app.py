from flask import Flask
from extensions import db, bcrypt, login_manager, migrate, ckeditor
from models import User  # Importar el modelo de usuario
import os


def create_app():
    # Inicializar la aplicación Flask
    app = Flask(__name__, instance_relative_config=True)

    # Crear la carpeta instance si no existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Configuración de la aplicación
    app.config['SECRET_KEY'] = 'supersecretkey'

    # Configuración de la base de datos SQLite en la carpeta instance
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Configuración para cargar imágenes
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'profile_pics')

    # Inicializar las extensiones con la aplicación
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)

    # Configuración del login manager
    login_manager.login_view = 'main.login'  # Nombre de la vista donde se redirige si no está autenticado
    login_manager.login_message_category = 'info'

    # Definir la función user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar Blueprints
    from routes import main
    app.register_blueprint(main)

    return app


# Crear la aplicación usando la función create_app
app = create_app()

# Ejecutar la aplicación en modo debug
if __name__ == '__main__':
    app.run(debug=True)
