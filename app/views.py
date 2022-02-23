# -*- coding: utf-8 -*-

# import os
import re
import time
import logging


from flask import render_template, flash, redirect, request, url_for, g, session, jsonify, abort, Response
from app import app

from .quickflask.visualization.vis_views import vis_view

logger = logging.getLogger(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = 'Anonymous'
    title = 'Index'
    return render_template("index.html",
        title = title,
        user = user)

@app.route('/vis/<path:code>', methods=['GET', 'POST'])
@app.route('/vis/<path:code>/<path:code2>', methods=['GET', 'POST'])
def vis_dispatch(code, code2=''):
    return vis_view(code, code2, request)

