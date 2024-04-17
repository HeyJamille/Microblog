from app import app
from flask import render_template #Importação para renderizar templates

@app.route('/')
@app.route('/index')
def index():
  nome = "Jamille"
  dados = {"nome": "Jamille", "idade": "20"}
  return render_template("index.html", nome=nome, dados=dados) # Chama o arquivo index.html

@app.route('/contato')
def contato():
  dados = {"email": "Jamille.araujo@gmail.com", "telefone": "(85) 99906-3736", "github": "HeyJamille"}
  return render_template("contato.html", dados=dados)

