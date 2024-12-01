from flask import Flask, render_template

# Criação do aplicativo Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return render_template('index.html')

# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)

