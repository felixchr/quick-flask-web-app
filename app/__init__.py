import os
import yaml

from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_apscheduler import APScheduler
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate()
migrate.init_app(app, db)

@app.context_processor
def inject_stage_and_region():
    here = os.path.abspath(os.path.dirname(__file__))
    about = {}
    with open(os.path.join(here, '../__version__.py'), 'r') as f:
        exec(f.read(), about)
    return {'about': about}

# lm = LoginManager()
# lm.init_app(app)

# sched = APScheduler()
# sched.init_app(app)
# sched.start()

from app import views, models
