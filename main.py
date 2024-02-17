from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index/<input_title>")
def index(input_title):
    return render_template("index.html", title=input_title)


if __name__ == "__main__":
    app.run()