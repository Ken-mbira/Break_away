from flask import Blueprint
from flask_restful import Api

main = Blueprint('main',__name__,url_prefix='/main')
api = Api(main,catch_all_404s=True)

from . import user_models,user_views