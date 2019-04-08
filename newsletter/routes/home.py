from flask import Blueprint, render_template
from newsletter.models.WpDatabases import WpDatabases

Home = Blueprint( 'Home', __name__ )

@Home.route('/')
def index():
    databases = WpDatabases()
    data = databases.find()
    return render_template( "home.html" )