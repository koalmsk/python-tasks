from flask import Flask, render_template



STAFF = "инженер", "строитель"

app = Flask(__name__)


@app.route("/training/<prof_input>")
def index(prof_input):
    to_page = (
        ("Инженерные тренажеры", "/static/imges/it.jpeg") if prof_input.lower() in STAFF 
        else ("Научные симуляторы", "/static/imges/ns.jpeg")
        )
    return render_template("index.html", prof=to_page[0], photo=to_page[1])


if __name__ == "__main__":
    app.run()