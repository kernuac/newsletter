from newsletter.models.post import Post

class Posts:
    def __init__( self ):
        self.__model = None
        self.__prefix = ''

    def set_model( self, model ):
        self.__model = model

    def set_prefix( self, prefix ):
        self.__prefix = prefix

    def get_prefix( self ):
        return self.__prefix

    def find_last_posts( self ):
        posts = []
        result = self.__find_posts()        

        for row in result:
            post = Post()

            post.set_id( row[ 'ID' ] )
            post.set_date( row[ 'date' ] )
            post.set_title( row[ 'title' ])
            post.set_url( row[ 'url' ] )
            post.set_content( self.__get_post_content( row[ 'ID' ] ) )
            post.set_featured_img( self.__get_featured_img( row[ 'ID' ] ) )
            
            posts.append( post )

        return posts

    def __get_featured_img( self, postid ):
        thumbnail_id = int( self.__get_thumbnail_id( postid ) )

        query = """
            select 
                pst.guid as img_url 
            from {}posts as pst
            where 
                id = {}
        """.format( self.get_prefix(), thumbnail_id )
        
        result = self.__model.execute( query )

        if not result:
            return ''

        return result[0][ 'img_url' ]

    def __get_thumbnail_id ( self, postid ):
        query = """
            select 
                pmt.meta_value as img_id
            from {}postmeta as pmt
            where
                post_id = {}
                and meta_key = '_thumbnail_id'
        """.format( self.get_prefix(), postid )

        result = self.__model.execute( query )

        if not result:
            return 0

        return result[0][ 'img_id' ]

    def __get_post_content( self, postid ):
        return []

    def __find_posts( self, limit=10 ):
        query = """
            select 
                pst.ID as ID, 
                pst.post_date as date, 
                pst.post_title as title, 
                pst.guid as url
            from {}posts as pst
            where 
                post_type = 'post' 
                and post_status = 'publish' order
                by ID desc limit {}
        """.format( self.get_prefix(), limit )

        result = self.__model.execute( query )

        return result