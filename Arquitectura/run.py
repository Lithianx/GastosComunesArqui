from app import create_app
from views.GastoComunView import gastos_blueprint


app = create_app()
app.register_blueprint(gastos_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
