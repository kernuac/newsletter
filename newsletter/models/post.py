class Post:
    def __init__( self ):
        self.__id = None
        self.__url = ''
        self.__date = ''
        self.__title = ''
        self.__content = ''
        self.__featured_img = ''

    def get_id ( self ):
        return self.__id

    def set_id ( self, postid ):
        self.__id = postid

    def get_url ( self ):
        return self.__url

    def set_url ( self, posturl ):
        self.__url = posturl

    def get_date ( self ):
        return self.__date

    def set_date( self, datetime ):
        self.__date = datetime

    def get_title( self ):
        return self.__title

    def set_title( self, title ):
        self.__title = title
        
    def get_content ( self ):
        return self.__content

    def set_content ( self, content ):
        self.__content = content

    def get_featured_img ( self ):
        return self.__featured_img

    def set_featured_img( self, imgurl ):
        self.__featured_img = imgurl