from tinydb import TinyDB, Query

# connecting the db
db = TinyDB( 'db.json' )
html = ''
search = Query()
for item in db.search(search.status == 'open'):
  title = item.get('ticket')
  description = item.get('ticket_description')
  html_string = '<div class="jumbotron"><h1 class="display-4">' + str(title) + '</h1><p class="lead">' + str(description) + '</p><hr class="my-4"><p class="lead"><a class="btn btn-primary btn-lg" href="https://39030.wayscript.io/reviewticket?title=' + str(title) + '" role="button">Learn more</a></p></div>'
  html = html + html_string

variables['html'] = html
