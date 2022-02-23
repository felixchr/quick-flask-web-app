#!/usr/bin/env python3

import logging

from app import app

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(process)d %(name)s] %(levelname)s %(message)s')
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)