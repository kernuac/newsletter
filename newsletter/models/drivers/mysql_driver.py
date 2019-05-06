import mysql.connector

class MysqlDriver:
    def __init__( self ):
        self.__host = ''
        self.__port = 0
        self.__user = ''
        self.__pass = ''
        self.__conn = None
        self.__cursor = None

    def __connect( self ):
        self.__conn = mysql.connector.connect(
            host=self.get_host(),
            user=self.get_user(),
            passwd=self.get_passwd(),
            database=self.get_database()
        )
        self.__cursor = self.__conn.cursor( dictionary=True )

    def __close( self ):
        self.__cursor = None
        self.__conn.close()

    def set_host( self, host ):
        self.__host = host
    
    def get_host( self ):
        return self.__host

    def set_port( self, port ):
        self.__port = port

    def get_port( self ):
        return self.__port

    def set_user( self, user ):
        self.__user = user

    def get_user( self ):
        return self.__user

    def set_passwd( self, passwd ):
        self.__pass = passwd

    def get_passwd( self ):
        return self.__pass

    def get_prefix( self ):
        return self.__prefix

    def set_prefix( self, dbprefix ):
        self.__prefix = dbprefix

    def get_database ( self ):
        return self.__database

    def set_database( self, database ):
        self.__database = database

    def execute( self, query, args=() ):
        self.__connect()
        
        self.__cursor.execute( query, args )
        data = self.__cursor.fetchall()
        self.__close()
        return data
    

    