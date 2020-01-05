from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/day")
def day():
    return "today is monday"
@app.route("/year")
def year():
    return "welcome to 2020"
app.run(debug=True)