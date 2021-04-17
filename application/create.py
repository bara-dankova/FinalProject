# This file should be run manually (directly) to manipulate the database
# The database must exist before connecting to it

from application import db
from application.models import TestTable

#create the database schema
db.create_all()

test1 = TestTable(first_name='Dolapo')
test2 = TestTable(first_name='Shaeera')
test3 = TestTable(first_name='Michaela')

db.session.add(test1)
db.session.add(test2)
db.session.add(test3)
db.session.commit()
