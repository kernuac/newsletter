import sqlite3, os

class SqliteDriver:
    def __init__( self ):
        self.__file = ''
        self.__conn = None
        self.__cursor = None

    def __connect ( self ):
        current_path = os.getcwd()
        path = os.path.join( current_path, 'newsletter/data' )

        self.__conn = sqlite3.connect( 
            os.path.join( path, self.get_filedb() ) 
        )

        self.__cursor = self.__conn.cursor()

    def __close( self ):
        self.__cursor = None
        self.__conn.close()

    def execute( self, query, args ):
        self.__connect()

        result = self.__cursor.execute( query, args )
        data = []
        columns = [ column[0] for column in result.description ]

        for row in result.fetchall():
            data.append( dict( zip( columns, row ) ) )

        self.__close()

        return data

    def set_filedb( self, filedb ):
        self.__file = filedb

    def get_filedb( self ):
        return self.__file
