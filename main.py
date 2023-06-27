"""Defines the API routes."""

import json

from flask import Flask, jsonify, abort, request

app = Flask(__name__)

with open("companies.json", "r") as f_obj:
    companies = json.load(f_obj)


def get_companies(companies, country=None):
    if country:
        return jsonify([c for c in companies if c["country"] == country])
    return jsonify(companies)


@app.route("/", methods=["GET"])
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/company", methods=["GET", "POST"])
def company(): # Get all or create one
    if request.method == "GET":
        params = request.args
        print(params)
        if "country" in params:
            return get_companies(companies, params["country"])
        return get_companies(companies)
    else:  # If it's a POST, someone is trying to add a new company
        
        new_company = request.json

        print(new_company)

        if "name" not in new_company or "country" not in new_company:
            abort(400)

        # Add it to the companies object
        companies.append(new_company)

        # Return success/failure
        return jsonify(new_company)


@app.route("/company/<int:id>", methods=["GET"])
def single_company(id):
    if id > len(companies):
        abort(404)
    return jsonify([c for c in companies if c["id"] == id][0])


@app.get("/stories")
def test():
    print(request.args)
    return "Help"

@app.errorhandler(404)
def error_not_found(args):
    return "<h1>404!</h1>"

@app.errorhandler(400)
def error_bad_request(args):
    return jsonify({
                "error": "Invalid data"
            }), 400


if __name__ == "__main__":
    app.run(port=5050, debug=True)