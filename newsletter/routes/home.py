from flask import Blueprint, render_template

Home = Blueprint( 'Home', __name__ )

@Home.route('/')
def index():
    return render_template( "home.html" )