from newsletter.etc.dbconfig import mysqldb, sqlitedb
from newsletter.models.WpDatabases import WpDatabases
from newsletter.models.posts import Posts

class NewsLetters:
    def __get_databases( self ):
        m_wp_databases = WpDatabases()
        databases = m_wp_databases.find()
        return databases

    def get_dashboard( self ):
        databases = self.__get_databases()
        dashboard = []
        for database in databases:
            dashboard.append( {
                'name' : database['name'],
                'data' : self.__get_individual_dashboard( database )
            } )
        return dashboard

    def __get_individual_dashboard( self, database ):
        mysqldb.set_host( database[ 'dbhost' ] )
        mysqldb.set_user( database[ 'dbuser'] )
        mysqldb.set_passwd( database[ 'dbpass' ] )
        mysqldb.set_database( database[ 'dbdatabase' ] )

        mPosts = Posts()
        mPosts.set_prefix ( database[ 'dbprefix' ] )
        mPosts.set_model( mysqldb )
        
        result = mPosts.find_last_posts()

        return result