# This file should be run manually (directly) to manipulate the database
# The database must exist before connecting to it

from application import db
# from application.models import TestTable
from application.models import Contestant, Song
from datetime import date

#create the database schema
db.drop_all()
db.create_all()

vincent = Contestant(first_name="Vincent", last_name="Bueno", pronoun="He/Him", dob=date(1985, 12, 10), country="Austria")
elena = Contestant(first_name="Vincent", last_name="Bueno", pronoun="He/Him", dob=date(1985, 12, 10), country="Austria")
db.session.add(vincent)
db.session.add(elena)
db.session.commit()

# Elena 	Tsagrinou	She/Her	16-Nov-94	Greece

song = Song(contestant_id=vincent.contestant_id, song_name="Concerto")

db.session.add(song)
db.session.commit()


# test1 = TestTable(first_name='Victoria')
# test2 = TestTable(first_name='Shaeera')
# test3 = TestTable(first_name='Michaela')
#
# db.session.add(test1)
# db.session.add(test2)
# db.session.add(test3)
# db.session.commit()
