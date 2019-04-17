from flask_restful import Resource
from flask_jwt import JWT, jwt_required, current_identity

class Login( Resource ):
    def post( self ):
        return { 'message' : "Request Login" }

class Logout( Resource ):
    def post( self ):
        return { 'message' : "Request Logout" }
        
