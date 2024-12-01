from app import app
from flask import render_template

# Rota principal
@app.route('/')
def home():
    return render_template("index.html")

@app.route("/teste")
def teste():
  return "nucktow"