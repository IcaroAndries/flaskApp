from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<page>')
def hello_world(page):
    return f"Hello, {escape('teste')}"