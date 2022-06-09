from fileinput import filename
from flask import Flask, render_template, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('views/hello.html')

@app.route('/<page>')
def hello_world(page):
    return f"Hello, {escape('teste')}"