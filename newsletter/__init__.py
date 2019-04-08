from flask import Flask
from flask_restful import Api

from newsletter.etc.conf import DevelopConfig

from newsletter.routes.home import Home
from newsletter.routes.admin import Admin

from newsletter.api import auth

app = Flask( __name__ )
apiv1 = Api( app, prefix='/api/v1' )

app.config.from_object( DevelopConfig )

# api endpoints
apiv1.add_resource ( auth.Login, '/login' )
apiv1.add_resource ( auth.Logout, '/logout' )

# app endpoints
app.register_blueprint( Admin, url_prefix='/admin')
app.register_blueprint( Home )
