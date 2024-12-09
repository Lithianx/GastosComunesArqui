from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    SingletonDB(app)  # Instancia Singleton de la BD

    # Importa el modelo y las vistas del módulo de gastos comunes
    with app.app_context():
        from models.GastoComunModel import GastoComun   # Importa el modelo específico
        #from views.GastoComunView import gastos_blueprint  # Importa el Blueprint para las rutas
        db.create_all()  # Crea las tablas en la base de datos si no existen

    # Registra el Blueprint para las rutas de gastos comunes
    #app.register_blueprint(gastos_blueprint)

    return app