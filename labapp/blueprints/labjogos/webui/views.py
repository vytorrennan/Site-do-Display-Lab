from flask import abort, render_template
from labapp.model.labjogos import Cargo, Colaboradores, Biblioteca, Projeto, \
    Games, DisplayCast, Projeto_Games, Projeto_DisplayCast

def home():
    return render_template("home.html")

def projetos():
    return render_template("projetos.html")

def institucional():
    return render_template("institucional.html")

def sobre():
    return render_template("sobre.html")

# Projetos

def exterminandoDrogas():
    return render_template("postsProjetos/exterminandoDrogas.html")

def displayCast():
    return render_template("postsProjetos/displayCast.html")