from flask import (
    Blueprint, flash, g, redirect, render_template, session, url_for, request
)

from .db import get_db

bp = Blueprint('redirect', __name__)

@bp.route('/s/<short_code>', methods=('GET',))
def redirect_to_url(short_code):
    db = get_db()
    row = db.execute(
        'SELECT original_url FROM shrink_tb WHERE shrink_code == (?)',
        (short_code,)
    ).fetchone()

    if row is None:
        return redirect(url_for('shrink.index'))

    original_url = row['original_url']
    return redirect(original_url)
