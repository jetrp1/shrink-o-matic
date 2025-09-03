from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for, request
)



from .db import get_db


bp = Blueprint('shrink', __name__, url_prefix='/shrink')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'GET':
        return render_template('shrink/shrink.html')
    elif request.method == 'POST':
        url = request.form['url']
        shrunk_url = shrink_url(url)
        shrink_bundle = {
            'shrunk_url': shrunk_url,
            'original_url': url
        }

        return render_template('shrink/shrunk.html', shrink=shrink_bundle)

def shrink_url(url):
    db = get_db()
    # does a shrink already exist for this URL?
    existing = db.execute(
        'SELECT shrink_code FROM shrink_tb WHERE original_url == (?)',
        (url,)
    ).fetchone()

    if existing is not None:
        return request.host_url + 's/' + existing['shrink_code']

    shrink_code = gen_shrink_code()
    while is_shrink_taken(shrink_code):
        shrink_code = gen_shrink_code()

    # add to database
    db.execute(
        'INSERT INTO shrink_tb (original_url, shrink_code) VALUES (?, ?)',
        (url, shrink_code)
    )
    db.commit()

    # Generate shrunk url
    prefix = request.host_url + 's/'
    return prefix + shrink_code

def gen_shrink_code():
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def is_shrink_taken(shrink_code):
    db = get_db()
    return db.execute(
        'SELECT id FROM shrink_tb WHERE shrink_code = ?', (shrink_code,)
    ).fetchone() is not None