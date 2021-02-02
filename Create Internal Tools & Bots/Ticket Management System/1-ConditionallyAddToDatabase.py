ticket_title = variables['ticket_title']
ticket_description = variables['description']

from tinydb import TinyDB, Query

db = TinyDB( 'db.json')
db.insert({'ticket': ticket_title, 'ticket_description': ticket_description, 'status':'open' })
