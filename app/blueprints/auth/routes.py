from flask import render_template

from . import bp

@bp.route('/signin')
def signin():
    return render_template('signin.jinja')

@bp.route('/register')
def register():
    return render_template('register.jinja')