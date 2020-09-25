# import the necessary packages

from app import app, q, db
from flask import redirect,render_template,url_for
from redis import Redis
import flask 
from .tasks import count_words_at_url
from app.models import Url

@app.route("/url", methods=["POST","GET"])
@app.route("/", methods=["POST","GET"])
def url():

    if flask.request.method == "POST":
        submited_url = flask.request.form["url"]              
        url_count = q.enqueue(count_words_at_url, result_ttl = 10, ttl = 10, args=(submited_url,))
               
    return render_template("submit_url.html")


@app.route("/index", methods=["GET"])
def index():
    url_details = Url.query.all()

    return render_template("index.html", url_details = url_details)

