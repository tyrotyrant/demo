from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required




# Views
@main.route('/')
def index():
    title = 'events'

    return render_template('index.html' )
