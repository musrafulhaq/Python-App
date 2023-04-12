from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, I'm testing in ewm....for integrating EWM to github"

if __name__ == "__main__":
    app.run(debug=True)
