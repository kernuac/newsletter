from flask import Flask
from newsletter.etc.conf import DevelopConfig

from newsletter.routes.home import Home

app = Flask( __name__ )

app.config.from_object( DevelopConfig )
app.register_blueprint( Home )
