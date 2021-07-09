from boot import constants
from ap import *
from flask import Flask, json, render_template, jsonify
from flask_cors import cross_origin
app = Flask(__name__, template_folder='site/build',
            static_folder='site/build/static')
constants = constants()


@app.route("/america")
@cross_origin()
def america():
    metarmap().america()
    return jsonify({"status": "success"})


@app.route("/metars")
@cross_origin()
def metar():
    metarmap().metars()
    return jsonify({"status": "success"})


@app.route("/red")
@cross_origin()
def red():
    metarmap().red()
    return jsonify({"status": "success"})


@app.route("/blue")
@cross_origin()
def blue():
    metarmap().blue()
    return jsonify({"status": "success"})


@app.route("/green")
@cross_origin()
def green():
    metarmap().green()
    return jsonify({"status": "success"})


@app.route("/off")
@cross_origin()
def off():
    print(constants.ip)
    metarmap().clear()
    return jsonify({"status": "success"})


@app.route("/")
@cross_origin()
def host():
    return render_template("index.html", serverip=constants.ip)


def run():
    app.run(host="0.0.0.0", port=3333)
