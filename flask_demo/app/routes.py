from flask import render_template, request, flash
from app.forms import SignupForm
from app import app
import requests
import json

def send_to_google( first_name, last_name, email ): 
	variables = json.dumps( [ first_name, last_name, email ] )
	url = 'https://wayscript.com/api'

	params = { 'api_key' : 'a2PbceI59A1989lHf2-T1-HTIhGXXypDK5FdxuHmJgw', 
			   'program_id' : 5353, 
			   'variables' : variables }

	requests.post( url, params = params )

@app.route( '/', methods = [ 'GET', 'POST' ] )
@app.route( '/index', methods = [ 'GET', 'POST' ] )
def index():
	signup_form = SignupForm()
	if signup_form.validate_on_submit(): 
		first_name = signup_form.first_name.data
		last_name = signup_form.last_name.data
		email = signup_form.email.data

		send_to_google( first_name, last_name, email )

		print( '\n', first_name, last_name, email, '\n' )		

	return render_template( 'index.html', signup_form = signup_form )