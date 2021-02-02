from tinydb import TinyDB, Query
title = variables['title']

db = TinyDB( 'db.json' )
search = Query()
db.update({'status': 'closed'}, search.ticket == title)
