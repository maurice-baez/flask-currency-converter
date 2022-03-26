from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"

@app.get("/")
def start():

    return render_template("index.html")

