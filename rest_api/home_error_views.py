from flask import render_template
from rest_api import app


# Handle missing pages
@app.errorhandler(404)
def page_not_found(e):
    return "404. The resource could not be found.", 404


# Endpoint for the homepage
@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
