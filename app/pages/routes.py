from flask import render_template
from app.pages import bp

@bp.route('/')
def home():
    return render_template('pages/home.html')

@bp.route('/projects')
def projects():
    return render_template('pages/projects.html')

@bp.route('/institutional')
def institutional():
    return render_template('pages/institutional.html')

@bp.route('/about')
def about():
    return render_template('pages/about.html')