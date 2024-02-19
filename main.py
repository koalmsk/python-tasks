import flask


app = flask.Flask(__name__)

PROFI_LIST = [
    "инженер-исследователь",
    "пилот",
    "строитель",
    "экзобиолог",
    "врач",
    "инженер по терраформированию",
    "климатолог",
    "специалист по радиационной защите",
    "астрогеолог",
    "гляциолог",
    "инженер жизнеобеспечения",
    "метеоролог",
    "оператор марсохода",
    "киберинженер",
    "штурман",
    "пилот дронов", 
]


@app.route("/")
def index():
    return "Миссия Колонизация Марса"


@app.route("/index")
def apples():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion_image")
def promotion():
    return flask.render_template("index.html")

@app.route("/anketa")
def anketa():
    return flask.render_template("registr.html", for_check_box=PROFI_LIST)
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=1)