import os

from flask import Flask

def create_app( test_config=None ):
    app = Flask( __name__, instance_relative_config=True )

    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
        DATABASE=os.path.join(
            app.instance_path, 'newsletter.db'
        )
    )

    if test_config is None:
        app.config.from_pyfile( 'config.py', silent=True )
    else:
        app.config.from_mapping( test_config )

    try:
        os.makedirs( app.instance_path )
    except OSError:
        pass

    from newsletter.routes.admin import Admin
    app.register_blueprint( Admin, url_prefix='/admin' )

    from newsletter.routes.newsletters import Newsletters
    app.register_blueprint( Newsletters, url_prefix='/newsletters' )

    from newsletter.routes.home import Home
    app.register_blueprint( Home )


    return app
#from flask import Flask
#from flask_restful import Api
#from flask_jwt import JWT, jwt_required, current_identity

#from newsletter.etc.conf import DevelopConfig

#from newsletter.routes.home import Home
#from newsletter.routes.admin import Admin

#from newsletter.api import auth

#from newsletter.etc.dbconfig import sqlitedb

#from newsletter.services.auth import request_token, identify

#app = Flask( __name__ )
#apiv1 = Api( app, prefix='/api/v1' )

#app.config.from_object( DevelopConfig )
#app.config['SECRET_KEY'] = 'super-secret'


# JWT
#jwt = JWT( app, request_token, identify )

# api endpoints
#apiv1.add_resource ( auth.Login, '/login' )
#apiv1.add_resource ( auth.Logout, '/logout' )

# app endpoints
#app.register_blueprint( Admin, url_prefix='/admin')
#app.register_blueprint( Home )
