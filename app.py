from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! :)'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


def convert_fahrenheit_to_celsius(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


@app.route('/f/<celsius>')
def convert_celsius(celsius):
    fahrenheit = convert_fahrenheit_to_celsius(float(celsius))
    return f'{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit'


if __name__ == '__main__':
    app.run()
