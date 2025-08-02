from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for, request
)

from .db import get_db

bp = Blueprint('shrink', __name__, url_prefix='/shrink')

@bp.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass


def gen_shrink_code():
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def is_shrink_taken(shrink_code):
    db = get_db()
    db.execute(
        'SELECT shrink_code FROM shrink_tb WHERE shrink_code == (?)',
        (shrink_code,)
    )