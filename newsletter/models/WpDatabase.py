from newsletter import app

class WpDatabase:
    def __init__( self ):
        self.__mwpdatabase = None

    def set_wp_database_object ( self, wpdatabase ):
        self.__mwpdatabase = wpdatabase

    def create( self ):
        query = """
            insert into wpdatabases ( 
                name, 
                description, 
                dbhost, 
                dbuser,
                dbpass,
                dbport,
                dbdatabase,
                dbprefix
            )
            values( ?, ?, ?, ?, ?, ?, ?, ? )
        """
        pass
    
    def update( self ):
        pass

    def delete( self ):
        pass