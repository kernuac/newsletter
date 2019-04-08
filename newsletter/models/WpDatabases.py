#from newsletter import sqlitemodel
#from newsletter import 
from newsletter.etc.dbconfig import sqlitedb
class WpDatabases():
    def find( self ):
        query = """
            select * from wpdatabases where 1 = 1
        """
        data = sqlitedb.execute( query )
        return data