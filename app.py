from flask import Flask, render_template

# Criação do aplicativo Flask
app = Flask(__name__)
from views import *




# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

