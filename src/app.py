from flask import app, Flask, render_template

kfmportfolio = Flask(__name__)

@kfmportfolio.route("/")
def Home():
    return render_template('inicio.html', titulo='Home')

@kfmportfolio.route("/About")
def About():
    return render_template('sobremim.html', titulo='Sobre Mim')

@kfmportfolio.route("/Projects")
def Projects():
    return render_template('projetos.html', titulo='Projetos')


if __name__ == '__main__':
    kfmportfolio.run('0.0.0.0')