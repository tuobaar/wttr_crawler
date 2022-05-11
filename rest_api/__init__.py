import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

from . import home_error_views
from . import database_views
from . import interval_views
from . import multi_views
from . import single_views
