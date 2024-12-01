from pico import app

@app.route("/")
@app.route("/index")
def index():
    return '''
    <html>
      <head><title>Index</title></head>
      <body>
        <h1>Olá Mundos</h1>
      </body>
    </html>
    '''

@app.route("/teste")
def teste():
    return "Aqui é o teste"

