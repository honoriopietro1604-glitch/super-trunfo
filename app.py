from flask import Flask
import random
 
app = Flask(__name__)
cartas=["carta1","carta2"]
 
@app.route("/")
def index():
    return '''
        <h1>Bem-vindo ao Trunfo de Memes!</h1>
        <p>Abra um pacotinho e descubra a sua carta.</p>
        <a href="/pacotinho">Abrir pacotinho</a>
    '''

@app.route("/pacotinho")
def pacotinho():
    carta = random.choice(cartas)
    return f"<h1>Você recebeu a carta: {carta}</h1>"

app.run(debug=True)