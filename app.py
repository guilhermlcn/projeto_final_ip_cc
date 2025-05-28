from click import prompt
from flask import Flask, render_template, request, url_for, redirect
import csv
import os
from google import genai
from google.genai import types

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


@app.route('/novo_termo')
def novo_termo():
    return render_template('novo_termo.html')

@app.route('/criar_termo', methods=['POST'])
def criar_termo():
  termo = request.form['termo']
  definicao = request.form['definição']

  with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow([termo, definicao])

  return redirect(url_for('glossario'))

@app.route('/chat_bot', methods=['POST'])
def chat_bot():
    prompt = request.form.get('prompt')
    resposta = None
    client = genai.Client(api_key="AIzaSyDAmIchF4JvyEfv4njinAlXTR886zJvz-w")
    modelo = 'gemini-2.0-flash'
    chat_config = {
        "system_instruction": "Você é um assistente pessoal, e sempre responde de forma objetiva."
}

    chat = client.chats.create(model=modelo, config=chat_config)

    resposta = chat.send_message(prompt)

    return render_template('chat_bot.html', resposta=resposta)

app.run()



