from flask import Blueprint

from newsletter.models.WpDatabases import WpDatabases 

Admin = Blueprint( 'Admin', __name__ )

@Admin.route( '/' )
def index():
    return "admin"

@Admin.route( '/databases' )
def get_databases_list():
    databases = WpDatabases() 
    return str( databases.find() )
