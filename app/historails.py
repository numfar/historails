# -*- coding: utf-8 -*-
import os
from flask import (
    Blueprint, render_template, current_app
)
from app.auth import login_required

bp = Blueprint('historails', __name__)

@bp.route('/')
def index():
    return render_template('index.html', token=current_app.config['ACCESS_TOKEN'])

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
