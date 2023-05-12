from flask import render_template, g

from . import bp
from app import app
from app.forms import UserSearchForm

@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()

@bp.route('/')
def home():
    matrix={
        'area': ('San Francisco', 'Oakland'),
        'types': ('Chinese','Seafood','Italian','Japanese')
    }
    return render_template('index.jinja',title='Home',area=matrix['area'],types=matrix['types'], user_search_form=g.user_search_form)

@bp.route('/about')
def about():
    return render_template('/about.jinja', user_search_form=g.user_search_form)