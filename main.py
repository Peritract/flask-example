"""Defines the API routes."""

import json

from flask import Flask, jsonify, abort, request  # The class that is a server

app = Flask(__name__)  # Make a server

with open("companies.json", "r") as f_obj:
    companies = json.load(f_obj)

@app.route("/", methods=["GET"])
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/company", methods=["GET"])
def company():
    params = request.args
    if "country" in params:
        return jsonify([c for c in companies if c["country"] == params["country"]])
    return jsonify(companies)


@app.route("/company/<int:id>", methods=["GET"])
def single_company(id):
    if id > len(companies):
        abort(404)
    return jsonify([c for c in companies if c["id"] == id][0])


@app.errorhandler(404)
def error_not_found(args):
    return "<h1>404!</h1>"


if __name__ == "__main__":
    app.run(port=5050, debug=True)