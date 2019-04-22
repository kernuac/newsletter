from newsletter.etc.dbconfig import sqlitedb

class Users:
    def find( self, args=[] ):
        query = """
            select user_id, username, passwd, email from users 
            where 1 = 1 
            """
        if len( args ) < 1:
            return sqlitedb.execute( query, args )

        values = [ fl[1] for fl in args ]
        values = tuple( values )

        for f in args:
            query = query + " and " + str( f[0] )

        return sqlitedb.execute( query, values )

    def find_by_user_passwd(self, username, passwd ):
        return self.find([
            [ 'username = ?', username ],
            [ 'passwd = ?', passwd ]
        ])

    def get_by_id( self, userid ):
        return self.find([
            ['user_id = ?', userid]
        ])[0]