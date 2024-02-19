import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return "Миссия Колонизация Марса"


@app.route("/index")
def apples():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion_image")
def promotion():
    return flask.render_template("index.html")
    


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=1)