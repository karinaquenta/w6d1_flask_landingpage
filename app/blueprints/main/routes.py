from flask import render_template

from . import bp

@bp.route('/')
def home():
    matrix={
        'area': ('San Francisco', 'Oakland'),
        'types': ('Chinese','Seafood','Italian','Japanese')
    }
    return render_template('index.jinja',title='Home',area=matrix['area'],types=matrix['types'])

@bp.route('/about')
def about():
    return render_template('/about.jinja')