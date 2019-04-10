from flask import Blueprint, render_template

from newsletter.models.WpDatabases import WpDatabases 

Admin = Blueprint( 'Admin', __name__ )

@Admin.route( '/' )
def index():
    return "admin"

@Admin.route( '/databases' )
def get_databases_list():
    databases = WpDatabases() 
    data = databases.find()
    return render_template( 
        'admin/databaseslist.html', data=data
    )

@Admin.route( '/<id_wpdb>/edit' )
def edit_databases( id_wpdb ):
    databases = WpDatabases()
    database = databases.get_by_id( id_wpdb )

    return render_template(
        'admin/editdatabase.html', database=database
    )
