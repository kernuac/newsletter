from flask import Blueprint, render_template, url_for, request
from newsletter.controllers.newsletters import NewsLetters

Newsletters = Blueprint( 'Newsletters', __name__ )

@Newsletters.route( '/' )
def dashboard():
    return "dashboard"

@Newsletters.route( '/new' )
def frm_new_newsletter( ):
    cnl = NewsLetters()
    cnl.get_dashboard()
    return "form new newsletter"