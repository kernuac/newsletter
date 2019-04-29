from newsletter.etc.dbconfig import mssqldb

class NewsLetters:
    def __init__( self ):
        pass

    def create( self, newsletter ):
        pass

    def update ( self, newsletter ):
        pass

    def delete( self, newsletter):
        pass

    def find(self, filters=[] ):
        query = """
            select 
                ID_Newsletter as newsletter_id,
                fechaCreacion as created_at,
                FechaPublicacion as published_at,
                estado as published,
                titulo as title
            from nl_NewsLetter
            where 1 = 1
        """
        
        if ( len( filters ) < 1 ):
            return mssqldb.execute( query )

        values = [ fl[ 1 ] for fl in filters ]
        values = tuple( values )

        for f in filters:
            query = query + " and " + str ( f[0] )

        return mssqldb.execute( query, values )
