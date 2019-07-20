from flask import Flask

app = Flask('__name__')

from app import user
from app import maps
from app import lesson