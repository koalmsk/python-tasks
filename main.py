from flask import Flask, render_template
import flask


STAFF = "инженер", "строитель"
PROFI_LIST_CONST = [
    "инженер",
    "строитель", 
    "и бла", 
    "бла",
    "бла", 
    "бла", 
    "бла"
]

app = Flask(__name__)

@app.route("/index/<input_title>")
def index(input_title):
    return render_template("index.html", title=input_title)


@app.route("/training/<prof_input>")
def profi(prof_input):
    to_page = ("Инженерные тренажеры" if prof_input in STAFF else "Научные симуляторы")
    return render_template("training.html", prof=to_page)


@app.route("/list_prof/<prof_input>")
def profi_list(prof_input):
    if prof_input not in ["ol", "ul"]:
        return render_template("error.html")
    return render_template("profi.html", mode=prof_input, prof=PROFI_LIST_CONST)


if __name__ == "__main__":
    app.run()