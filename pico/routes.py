from pico import app
from flask import render_template

nome = "desfraça"


@app.route("/")
@app.route("/index")
def index():
  
    return render_template("index.html")

@app.route("/teste")
def teste():
    return "Aqui é o teste"

