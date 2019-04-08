class MWpDatabase:
    def __init__( self ):
        self.__id = 0
        self.__name = ''
        self.__description = ''
        self.__dbhost = ''
        self.__dbuser = ''
        self.__dbpass = ''
        self.__dbport = ''
        self.__dbdatabase = ''
        self.__dbprefix = ''

    def get_id( self ):
        return self.__id

    def set_id ( self, idwpdb ):
        self.__id = idwpdb

    def get_description( self ):
        return self.__description

    def set_description ( self, description ):
        self.__description = description

    def get_host ( self ):
        return self.__dbhost

    def set_host( self, host ):
        self.__dbhost = host

    def get_user( self ):
        return self.__dbuser

    def set_user ( self, dbuser ):
        self.__dbuser = dbuser

    def get_passwd( self ):
        return self.__dbpass

    def set_passwd( self, dbpass ):
        self.__dbpass = dbpass

    def get_port ( self ):
        return self.__dbport

    def set_port ( self, dbport ):
        self.__dbport = dbport

    def get_database ( self ):
        return self.__dbdatabase

    def set_database( self, dbdatabase ):
        self.__dbdatabase = dbdatabase

    def get_prefix ( self ):
        return self.__dbprefix

    def set_prefix ( self, dbprefix ):
        self.__dbprefix = dbprefix