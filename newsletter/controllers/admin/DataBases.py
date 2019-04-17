from flask import render_template, url_for, request
from newsletter.models.WpDatabases import WpDatabases
from newsletter.models.MWpDatabase import MWpDatabase
import json

class DataBases:
    def showForm( self ):
        return []

    def show_edit_form( self ):
        title = "Nueva base de datos"
        method = 'POST'
        action = ''
        #action = url_for( 'api.new_wpdatabase' )
        return render_template(
            'admin/editdatabase.html', 
            database=[], 
            title=title,
            method=method,
            action=action
        )

    def create( self ):
        nwdb = MWpDatabase()

        nwdb.set_name( request.form.get( "txt_name" ) )
        nwdb.set_description( request.form.get( "txa_description" ) )
        nwdb.set_user( request.form.get( "txt_user" ) )
        nwdb.set_host ( request.form.get( "txt_dbhost" ) )
        nwdb.set_passwd( request.form.get( "pwd_dbpass" ) )
        nwdb.set_port( request.form.get( "txt_dbport" ) )
        nwdb.set_database( request.form.get( "txt_dbdatabase" ) )
        nwdb.set_prefix( request.form.get( "txt_dbprefix" ) )

        model = WpDatabases() 

        result = model.create( nwdb )

        if result < 1:
            return json.dumps({
                "status" : False,
                "message" : "No se pudo crear el nuevo registro"
            })

        return json.dumps({
            "status" : True,
            "message" : "Registro creado exitosamente"
        })
        