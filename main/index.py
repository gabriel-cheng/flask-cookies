from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message:": "Hello, world!"})

@app.route("/new_cookie")
def new_cookie():
    response = make_response("Hello world!")
    response.set_cookie("Name", "Gabriel")

    return response

@app.route("/show_cookie")
def show_cookie():
    cookie_value = request.cookies.get("Name")

    return cookie_value

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
