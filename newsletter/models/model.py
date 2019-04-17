class Model:
    def __init__( self ):
        self.__driver = None

    def set_driver ( self, driver ):
        self.__driver = driver
    
    def execute( self, query, args=None ):
        return self.__driver.execute( query, args )

    def single_query( self, query, args=None ):
        return self.__driver.single_query( query, args )