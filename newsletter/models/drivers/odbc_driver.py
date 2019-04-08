import pyodbc

class OdbcDriver:
    def __init__( self ):
        self.__conn = None
        self.__rdn = None
        self.__user = None
        self.__pass = None
        self.__port = None
        self.__cursor = None
    
    def set_rdn( self, rdn ):
        self.__rdn = rdn

    def get_rdn ( self ):
        return self.__rdn

    def set_user( self, user ):
        self.__user = user

    def get_user ( self ):
        return self.__user

    def set_passwd ( self, passwd ):
        self.__pass = passwd

    def get_passwd ( self ):
        return self.__pass

    def set_port ( self, port ):
        self.__port = port

    def get_port ( self ):
        return self.__port

    def __connect( self ):
        connection_string = "DSN=%s;UID=%s;PWD=%s" % ( 
            self.get_rdn(), self.get_user(), self.get_passwd() 
        )
        self.__conn = pyodbc.connect( connection_string )
        self.__cursor = self.__conn.cursor()

    def __close( self ):
        self.__cursor = None
        self.__conn.close()