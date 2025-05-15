from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def ola():
    return render_template('index.html')

@app.route('/sobre-equipe')
def alo():
    return render_template('sobre-equipe.html')

app.run()

