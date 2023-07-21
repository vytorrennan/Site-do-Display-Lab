from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template("postsProjetos/exterminandoDrogas.html")

@app.route("/projetos/displayCast")
def displayCast():
    return render_template("postsProjetos/displayCast.html")

@app.route("/projetos/educaRedes")
def educaRedes():
    return render_template("postsProjetos/educaRedes.html")

@app.route("/projetos/peruacuDigital")
def peruacuDigital():
    return render_template("postsProjetos/peruacuDigital.html")

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,  # Você pode especificar a porta desejada aqui, por exemplo, 5000
        debug=True  # Defina como False para desabilitar o modo de depuração
    )
