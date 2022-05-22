from flask import app, Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('inicio.html', titulo='Home')

@app.route("/About")
def About():
    return render_template('sobremim.html', titulo='Sobre Mim')

@app.route("/Projects")
def Projects():
    return render_template('projetos.html', titulo='Projetos')


if __name__ == '__main__':
    app.run('0.0.0.0')