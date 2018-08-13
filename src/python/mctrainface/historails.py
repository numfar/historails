# -*- coding: utf-8 -*-
import os
from flask import (
    Blueprint, render_template
)
from mctrainface.auth import login_required

bp = Blueprint('historails', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
