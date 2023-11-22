# encoding:utf-8
import requests
import logging
import json
import urllib
import re
try:
    from urllib.parse import urlparse
except:
     from urlparse import urlparse

from flask import jsonify, render_template, url_for, redirect, request, abort

from meta import app as application

@application.route("/index.html", endpoint="index")
@application.route("/", endpoint="index")
def index():
    return render_template('index.html', base_url=url_for("index"))

@application.route("/author", endpoint="author")
@application.route("/author/", endpoint="author")
def about():
    return render_template('author.html', base_url=url_for("author"))

@application.route("/about", endpoint="about")
@application.route("/about/", endpoint="about")
def about():
    # About the project
    return render_template('about.html', base_url=url_for("about"))


