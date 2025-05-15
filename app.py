from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre_equipe')
def alo():
    return render_template('sobre_equipe.html')

app.run()

