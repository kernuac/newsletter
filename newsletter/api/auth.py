from flask_restful import Resource

class Login( Resource ):
    def post( self ):
        return { 'message' : "Request Login" }

class Logout( Resource ):
    def post( self ):
        return { 'message' : "Request Logout" }
        
