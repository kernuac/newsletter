from newsletter.etc.dbconfig import sqlitedb

class WpDatabases():
    def find( self, filters=[] ):
        query = """
            select * from wpdatabases where 1 = 1
        """
        
        if len( filters ) < 1:
            return sqlitedb.execute( query, filters )

        values = [ fl[1] for fl in filters ]
        values = tuple( values )

        for f in filters:
            query = query + " and " + str( f[0] )

        data = sqlitedb.execute( query, values )

        return data


    def get_by_id( self, id_wpdb ):
        return self.find( [['id_wpdb = ?', id_wpdb ]] )[0]

    def create( self, wpDatabase ):
        query = """
        insert into wpdatabases ( 
            name, 
            description, 
            dbhost, 
            dbuser,
            dbpass,
            dbport,
            dbdatabase,
            dbprefix
        )
        values ( ?, ?, ?, ?, ?, ?, ?, ? )
        """
        return sqlitedb.single_query( query, ( 
            wpDatabase.get_name(), 
            wpDatabase.get_description(),
            wpDatabase.get_host(),
            wpDatabase.get_user(),
            wpDatabase.get_passwd(),
            wpDatabase.get_port(),
            wpDatabase.get_database(),
            wpDatabase.get_prefix()
        ))
         
        