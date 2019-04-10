
class Model:
    def __init__( self ):
        self.__driver = None

    def set_driver ( self, driver ):
        self.__driver = driver
    
    def execute( self, query ):
        return self.__driver.execute( query )