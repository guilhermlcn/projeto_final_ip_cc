from flask import Flask, render_template, request, url_for
import csv
import os

from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre_equipe')
def alo():
    return render_template('sobre_equipe.html')

@app.route('/glossario')
def glossario():

    glossario_de_termos = []

    with open ('bd_glossario.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for t in reader:
            glossario_de_termos.append(t)

    return render_template('glossario.html', glossario=glossario_de_termos)


@app.route('/novo-termo')
def novo_termo():
    return render_template('novo-termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
  termo = request.form['termo']
  definicao = request.form['definição']

  with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([termo, definicao])

  return redirect(url_for('glossario'))
app.run()