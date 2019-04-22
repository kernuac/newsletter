class MUser:
    def __init__( self ):
        self.id = 0
        self.__user = ''
        self.__pass = ''

    def set_id ( self, id ):
        self.id = id
    
    def get_id ( self ):
        return self.id

    def set_user ( self, username ):
        self.__user = username

    def get_user ( self ):
        return self.__user

    def set_passwd ( self, passwd ):
        self.__passwd = passwd
    
    def get_passwd ( self ):
        return self.__passwd
