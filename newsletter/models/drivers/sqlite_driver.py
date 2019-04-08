import sqlite3

class SqliteDriver:
    def __init__( self ):
        self.__file = ''
        self.__conn = None
        self.__cursor = None

    def __connect ( self ):
        self.__conn = sqlite3.connect( self.get_filedb() )
        self.__cursor = self.__conn.cursor()

    def __close( self ):
        self.__cursor = None
        self.__conn.close()

    def execute( self, query ):
        self.__connect()
        data = self.__cursor.execute( query )
        self.__close()
        return data

    def set_filedb( self, filedb ):
        self.__file = filedb

    def get_filedb( self ):
        return self.__file
