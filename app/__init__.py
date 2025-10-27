from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar y registrar rutas
    from app.routes.mesa_routes import mesa_bp
    app.register_blueprint(mesa_bp, url_prefix='/api/mesa')

    return app
