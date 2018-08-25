# -*- coding: utf-8 -*-
import os
import json
from flask import (
    Blueprint, render_template, current_app
)
import sqlite3

from app.db import get_db
from app.crud.cruddymodule import Crudder
from app.auth import login_required

bp = Blueprint('historails', __name__)

@bp.route('/')
def index():
    conn = get_db()
    db = conn.cursor()
    crudder = Crudder(db)
    trainroutes = crudder.get_all_routes()
    geojson = []
    for tr in trainroutes:
        geojson.extend(tr.getAsGeojson())
    return render_template('index.html',
                           token=current_app.config['ACCESS_TOKEN'],
                           routes=json.dumps(geojson),
                           startYear=current_app.config['FROM_YEAR']);

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
