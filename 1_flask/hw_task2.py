from flask import Flask, request

# task 2

app = Flask(__name__)

@app.route('/')
def get_hello():
    return "Hello, Flask!"

@app.route('/user/', defaults={"name": "alice"})
@app.route('/user/<name>')
def get_name(name):
    return f"Hello, {name}"

if __name__ == "__main__":
    app.run(debug=True)