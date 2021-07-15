from ap import metarmap
import constants
from flask import Flask, json, render_template, jsonify, request
from flask_cors import cross_origin
app = Flask(__name__, template_folder='site/build',
            static_folder='site/build/static')


def run():
    print(constants.ip)
    app.run(host="0.0.0.0", port=3333)


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
    metarmap().clear()
    return jsonify({"status": "success"})


@app.route("/testAmount/<num>")
@cross_origin()
def testAmountamount(num):
    metarmap().testAmount(int(num))
    return jsonify({"status": "success"})


@app.route("/setAirports", methods=["POST"])
@cross_origin()
def airportsGetter():
    data = request.get_json()
    constants.setter(data)
    return jsonify({"status": "success"})


@app.route("/")
@cross_origin()
def host():
    print("IP is set to -> " + str(constants.ip))
    print("I found the airports but the list is long so I won't print it")
    return render_template("index.html", serverip=constants.ip)
