from flask import Flask, request

# task 1

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/homepage')
def home():
    return "Hello, homepage!"

@app.route('/homepage/post', methods=["POST"])
def post():
    requests_json = request.json
    name = requests_json["user_name"]
    return f"Hello, {name}! "


@app.route('/homepage/postform', methods=["POST"])
def postform():
    name = request.form["user_name"]
    age = request.form["age"]
    return f"Hello, {name}, you are {age}! "



if __name__ =='__main__':
    app.run(debug=True)


