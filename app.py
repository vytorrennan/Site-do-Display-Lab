from flask import Flask, render_template

#=======================================================================================================================
#                                               Banco de Dados - SQLite
#=======================================================================================================================

from flask_migrate import Migrate
import os

from models import db, Cargo, Colaboradores, Biblioteca, Projeto, Games, DisplayCast, Projeto_Games, Projeto_DisplayCast

app = Flask(__name__)

# Define o caminho absoluto para o arquivo do banco de dados SQLite
database_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database.db')

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path

db.init_app(app)
migrate = Migrate(app, db)

#=======================================================================================================================

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

@app.route("/institucional")
def institucional():
    return render_template("institucional.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# Projetos

@app.route("/projetos/exterminandoDrogas")
def exterminandoDrogas():
    return render_template("projetos/exterminandoDrogas.html")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,  # Você pode especificar a porta desejada aqui, por exemplo, 5000
        debug=True  # Defina como False para desabilitar o modo de depuração
    )
