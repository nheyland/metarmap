from ap import *
from flask import Flask, render_template
from flask_cors import cross_origin
app = Flask(__name__, template_folder='site/build',
            static_folder='site/build/static')


# @app.route("/america")
# @cross_origin()
# def america():
#     metarmap().america()
#     return "<p>success<P>"


# @app.route("/metars")
# @cross_origin()
# def metar():
#     metarmap().metars()
#     return "<p>success<P>"


# @app.route("/red")
# @cross_origin()
# def red():
#     metarmap().red()
#     return "<p>success<P>"


# @app.route("/blue")
# @cross_origin()
# def blue():
#     metarmap().blue()
#     return "<p>success<P>"


# @app.route("/green")
# @cross_origin()
# def green():
#     metarmap().green()
#     return "<p>success<P>"


# @app.route("/off")
# @cross_origin()
# def off():
#     metarmap().clear()
#     return "<p>success<P>"


@app.route("/")
@cross_origin()
def host():
    ip = "http://192.168.0.33:333"
    return render_template("index.html", serverip=ip)


def run():
    app.run(host="0.0.0.0", port=3333)


# run()
