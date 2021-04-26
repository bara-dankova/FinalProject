# This file should be run manually (directly) to manipulate the database
# The database must exist before connecting to it

from application import db
# from application.models import TestTable
from application.models import Contestant, Song, Blog
from datetime import date

#create the database schema
db.drop_all()
db.create_all()

vincent = Contestant(first_name="Vincent", last_name="Bueno", pronoun="He/Him", dob=date(1985, 12, 10), country="Austria")
elena = Contestant(first_name="Elena", last_name="Tsagrinou", pronoun="She/Her", dob=date(1994, 11, 16), country="Greece")
anxhela = Contestant(first_name="Anxhela", last_name="Peristeri", pronoun="She/Her", dob=date(1986, 3, 24), country="Albania")

db.session.add(vincent)
db.session.add(elena)
db.session.add(anxhela)
db.session.commit()

# Elena 	Tsagrinou	She/Her	16-Nov-94	Greece

song = Song(contestant_id=vincent.contestant_id, song_name="Concerto")
greek_song = Song(contestant_id=elena.contestant_id, song_name="Last Dance")
albania_song = Song(contestant_id=anxhela.contestant_id, song_name="Karma")
db.session.add(song)
db.session.add(greek_song)
db.session.add(albania_song)
db.session.commit()

blog1 = Blog(date_posted = date(2021, 4, 23),
             contestant_id = vincent.contestant_id,
             blog_title="A little bit about Vincent Bueno", blog_text="Bueno started dancing at the age of 4.[4] He later graduated in music and performing arts at the Vienna Conservatory of Music. Bueno is also a composer of R&B music, having taken special courses in acting, dancing, and singing. At age 11, he managed to play 4 musical instruments—piano, guitar, drums, and bass guitar. His father was a former vocalist and a 1970 local band lead guitarist.",
             blog_views = 0)
blog2 = Blog(date_posted = date(2021, 4, 26),
             contestant_id = anxhela.contestant_id,
             blog_title="A little bit about Anxhela Peristeri", blog_text="Anxhela Peristeri was born on 24 March 1986 into an Albanian family of the Eastern Orthodox faith in the city of Korce, then part of the People's Republic of Albania, present Albania.[1][2][3] Her grandfather is of Greek origin.[4][5] After graduating from high school in Tirana, Peristeri and her family moved to Greece.[6][7] Describing her life in the latter country, she had stated that she experienced discrimination because of her Albanian origin.[8][9] In December 2001, Peristeri unsuccessfully participated in the 40th edition of Festivali i Kenges with the song 'Vetem ty te kam'.[2] Later that year, she entered the Miss Albania national pageant in Tirana.[10][11] In June 2016, she emerged as the winner of the first season of Your Face Sounds Familiar.[12] Later, in December 2016, she debuted at Kenga Magjike with the song 'Genjeshtar', finishing in the second place.[13] Then in December 2017, she won the 19th edition of Kenga Magjike with the song 'E Cmendur'.[14]",
             blog_views = 0)

db.session.add(blog1)
db.session.add(blog2)
db.session.commit()


# test1 = TestTable(first_name='Victoria')
# test2 = TestTable(first_name='Shaeera')
# test3 = TestTable(first_name='Michaela')
#
# db.session.add(test1)
# db.session.add(test2)
# db.session.add(test3)
# db.session.commit()
