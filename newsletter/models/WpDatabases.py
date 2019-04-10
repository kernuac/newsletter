#from newsletter import sqlitemodel
#from newsletter import 
from newsletter.etc.dbconfig import sqlitedb
class WpDatabases():
    def find( self, filters=[] ):

        query = """
            select * from wpdatabases where 1 = 1
        """
        values = [ fl[1] for fl in filters ]
        values = tuple( values )

        for f in filters:
            query = query + " and " + str( f[0] )
        print ( query )
        print ( values )
        data = sqlitedb.execute( query, values )

        return data


    def get_by_id( self, id_wpdb ):
        return self.find( [['id_wpdb = ?', id_wpdb ]] )[0]