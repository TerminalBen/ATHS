from flask import Flask
app = Flask(__name__)

@app.route('/')

def beggining():
    return ('im just starting321315635')

if __name__ == '__main__':
    app.run()