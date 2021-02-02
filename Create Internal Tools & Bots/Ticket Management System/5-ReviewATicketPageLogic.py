from tinydb import TinyDB, Query
title = variables['title']

db = TinyDB( 'db.json' )
search = Query()
html = ''
for item in db.search(search.ticket == title):
  title = item.get('ticket')
  description = item.get('ticket_description')
  html_string = '<div class="jumbotron"><h1 class="display-4">' + str(title) + '</h1><p class="lead">' + str(description) + '</p><hr class="my-4"><p class="lead"><a class="btn btn-primary btn-lg" href="https://39030.wayscript.io/closingtickets?title=' + str(title) + '" role="button">Close</a></p></div>'
  html = html + html_string

variables['html_string'] = html
