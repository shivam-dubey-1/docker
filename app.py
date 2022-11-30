from flask import Flask
import os
app = Flask(__name__)

@app.route("/live")
def live():
    return "OK", 200;

@app.route("/hello")
def hello():
    message = os.getenv('MESSAGE', "Python")
    return "Hello " + message + " World\n!", 200;

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
