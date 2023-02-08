from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('hello')
def mein():
    return ('hello')

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
