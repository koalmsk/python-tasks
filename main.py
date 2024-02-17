from flask import Flask, render_template



STAFF = "инженер", "строитель"

app = Flask(__name__)


@app.route("/training/<prof_input>")
def index(prof_input):
    to_page = ("Инженерные тренажеры" if prof_input in STAFF else "Научные симуляторы")
    return render_template("index.html", prof=to_page)


if __name__ == "__main__":
    app.run()