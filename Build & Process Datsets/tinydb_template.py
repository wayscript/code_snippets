from tinydb import TinyDB, Query

# connecting the db
db = TinyDB( 'db.json' )

# inserting into the db
db.insert({'type': 'apple', 'count': 7})

# Getting all items in db
#db.all()

# Query the database
#Fruit = Query()
#db.search(Fruit.type == 'peach')

# Updating DB
#db.update({'count': 10}, Fruit.type == 'apple')

# Remove entries
#db.remove(Fruit.count < 5)
