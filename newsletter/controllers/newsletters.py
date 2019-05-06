from newsletter.etc.dbconfig import mysqldb, sqlitedb
from newsletter.models.WpDatabases import WpDatabases

class NewsLetters:
    def __get_databases( self ):
        m_wp_databases = WpDatabases()
        databases = m_wp_databases.find()
        return databases

    def get_dashboard( self ):
        databases = self.__get_databases()
        #for database in databases:
        #    self.__get_individual_dashboard( database )
        self.__get_individual_dashboard( databases[0] )

    def __get_individual_dashboard( self, database ):
        mysqldb.set_host( database[ 'dbhost' ] )
        mysqldb.set_user( database[ 'dbuser'] )
        mysqldb.set_passwd( database[ 'dbpass' ] )
        mysqldb.set_database( database[ 'dbdatabase' ] )
        mysqldb.set_prefix ( database[ 'dbprefix' ] )
        query = "select  from {}".format( "{}{}".format( mysqldb.get_prefix(), "posts" ) )
        print ( query )
        result = mysqldb.execute( query )
        print ( str( result ) )

    def __get_content( self, postid ):
        pass

    def __get_featured_image( self, postid ):
        pass
        
