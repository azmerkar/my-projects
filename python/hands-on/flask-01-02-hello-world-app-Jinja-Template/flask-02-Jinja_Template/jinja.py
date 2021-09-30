from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def head():
    return render_template('index.html', number1=20000, number2=40000)


@app.route('/mult')
def number():
    var1, var2 = 30, 70
    return render_template('body.html', value1=var1, value2=var2, value3=var1*var2)


if __name__ == '__main__':
    app.run(debug=True)
