from pico import app
from flask import render_template

nome = "desfraça"


@app.route("/")
@app.route("/index")
def index():
    jes = "brenus"
    return render_template("index.html", pico= jes )

@app.route("/teste")
def teste():
    return render_template("teste.html")

