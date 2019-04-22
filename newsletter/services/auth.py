import hashlib

from newsletter.etc.conf import DevelopConfig

from newsletter.models import Users, MUser

def request_token( username, password ):
    secret = hashlib.md5( DevelopConfig.SECRET.encode('utf-8') ).hexdigest()
    hashed = hashlib.md5( password.encode('utf-8') ).hexdigest()
    asdf = "%s.%s" % ( hashed, secret )
    pwd = hashlib.md5( asdf.encode( 'utf-8' )  ).hexdigest()
    
    users = Users.Users()
    user = MUser.MUser()

    data = users.find_by_user_passwd( username, pwd )
    
    if not data:
        return False
    
    user.set_id( data[0]['user_id'] )
    user.set_user( data[0]['username'] )
    user.set_passwd( data[0]['passwd'] )
 
    return user

def identify( payload ):
    user_id = payload['identity']
    
    users = Users.Users()
    user = MUser.MUser()

    data = users.get_by_id( user_id )

    if not data:
        return False

    user.set_id( data[ 'user_id' ] )
    user.set_user( data[ 'username' ] )

    return user
