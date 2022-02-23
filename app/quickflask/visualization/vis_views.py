import logging

from flask import request

logger = logging.getLogger(__name__)

def vis_view(code, code2, request:request):
    if code == 'table':
        pass
