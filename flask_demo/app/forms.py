from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm( FlaskForm ):
	first_name = StringField( 'First Name', 
		                      validators = [ DataRequired() ],
	                          render_kw = { 'placeholder': 'First Name' } )
	last_name = StringField( 'Last Name', 
							 validators = [ DataRequired() ], 
							 render_kw = { 'placeholder': 'Last Name' } )
	
	email =  StringField( 'Email', 
		                  validators = [ DataRequired(), Email() ], 
		                  render_kw = { 'placeholder': 'Email Address' } )
	
	submit = SubmitField( 'Sign Up' )