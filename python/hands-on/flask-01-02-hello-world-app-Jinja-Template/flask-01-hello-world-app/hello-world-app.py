from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Servus Welt von Flusk"


@app.route('/second')
def second():
    return "Überall sind doch für uns wie Trabzon"


@app.route('/third/subthird')
def third():
    return "Das ist die Unterseite von der dritte Seite"


@app.route('/forth/<string:id>')
def forth(id):
    return f'ID-Nummer von dieser Seite ist {id}'


if __name__ == '__main__':
    app.run(debug=True)
