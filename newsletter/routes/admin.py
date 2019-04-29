from flask import Blueprint, render_template, url_for, request
from newsletter.controllers.admin.DataBases import DataBases
from newsletter.models.WpDatabases import WpDatabases
from newsletter.models.Users import Users
from newsletter.models.nl.newsletters import NewsLetters

from flask_jwt import jwt_required, current_identity

Admin = Blueprint( 'Admin', __name__ )

@Admin.route( '/' )
def index():
    modules = [
        {
            "url" : url_for( 'Admin.get_databases_list' ),
            "label" : "Databases"
        },
        {
            "url" : url_for( 'Admin.get_newsletters' ),
            "label": "Newsletters"
        },
        {
            "url" : url_for( 'Admin.get_users' ),
            "label": "Usuarios"
        }
    ]
    return render_template(
        'admin/home.html', modules = modules
    )

@Admin.route( '/databases' )
def get_databases_list():
    databases = WpDatabases() 
    data = databases.find()

    return render_template( 
        'admin/databaseslist.html', data=data
    )

@Admin.route( '/databases/new', methods=['GET', 'POST'] )
def form_new_database():
    controller = DataBases()

    if request.method == 'POST':
        return controller.create()
    elif request.method == 'GET':
        return controller.show_edit_form()

@Admin.route( '/<id_wpdb>/edit' )
def edit_databases( id_wpdb ):
    databases = WpDatabases()
    database = databases.get_by_id( id_wpdb )

    title = "Editar base de datos %s" % ( database['name'] ) 
    
    return render_template(
        'admin/editdatabase.html', database=database, title=title
    )

@Admin.route( '/newsletters' )
def get_newsletters():
    mNewsletters = NewsLetters()
    newsletters = mNewsletters.find()
    title='Administración de Boletines'
    return render_template(
        'admin/newsletterslist.html',
        newsletters=newsletters, title=title
    )

@Admin.route( '/users' )
def get_users():
    musers = Users()
    users = musers.find()
    title="Administración de Usuarios"
    return render_template(
        'admin/userslist.html',
        users=users, title=title
    )

@Admin.route( '/users/new' )
def form_new_user():
    user=[]
    title = "Nuevo Usuario"
    return render_template(
        'admin/edituser.html',
        user=user, title=title
    )

@Admin.route( '/users/<int:user_id>/edit' )
def form_edit_user( user_id ):
    users = Users()
    user = users.get_by_id( user_id )
    title = "Editar Usuario"
    return render_template(
        'admin/edituser.html',
        user=user, title=title
    )


@Admin.route( '/newsletters/<int:newsletter_id>/edit' )
def form_edit_newsletter( newsletter_id ):
    return render_template( 'admin/editnewsletters.html' )

@Admin.route( '/newsletters/new' )
def form_new_newsletter():
    return render_template( 'admin/editnewsletters.html' )

