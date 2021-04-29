# This file should be run manually (directly) to manipulate the database
# The database must exist before connecting to it

# from application import db
# from application.models import TestTable
from application.models import *
from application.password import hash_password
from datetime import date, datetime

# create the database schema
db.drop_all()
db.create_all()

vincent = Contestant(first_name="Vincent", last_name="Bueno", pronoun="He/Him", dob=date(1985, 12, 10),
                     country="Austria")
elena = Contestant(first_name="Elena", last_name="Tsagrinou", pronoun="She/Her", dob=date(1994, 11, 16),
                   country="Cyprus")
anxhela = Contestant(first_name="Anxhela", last_name="Peristeri", pronoun="She/Her", dob=date(1986, 3, 24),
                     country="Albania")
uku = Contestant(first_name="Uku", last_name="Suviste", pronoun="He/Him", dob=date(1982, 6, 6), country="Estonia")
barbara = Contestant(first_name="Barbara", last_name="Pravi", pronoun="She/Her", dob=date(1993, 4, 10),
                     country="France")
eden = Contestant(first_name="Eden", last_name="Alene", pronoun="She/Her", dob=date(2000, 5, 7), country="Israel")
montaigne = Contestant(first_name="Uku", last_name="", pronoun="She/Her", dob=date(1995, 8, 14), country="Australia")
efendi = Contestant(first_name="Efendi", last_name="", pronoun="She/Her", dob=date(1991, 4, 17), country="Azerbaijan")
benny = Contestant(first_name="Benny", last_name="Cristo", pronoun="He/Him", dob=date(1987, 6, 8), country="Greece")
manizha = Contestant(first_name="Manizha", last_name="", pronoun="She/Her", dob=date(1991, 7, 8), country="Russia")

db.session.add(vincent)
db.session.add(elena)
db.session.add(anxhela)
db.session.add(uku)
db.session.add(barbara)
db.session.add(eden)
db.session.add(montaigne)
db.session.add(efendi)
db.session.add(benny)
db.session.add(manizha)
db.session.commit()

amen = Song(contestant_id=vincent.contestant_id, song_name="Amen")
el_diablo = Song(contestant_id=elena.contestant_id, song_name="El Diablo")
karma = Song(contestant_id=anxhela.contestant_id, song_name="Karma")
lucky_one = Song(contestant_id=uku.contestant_id, song_name="The Lucky One")
voila = Song(contestant_id=barbara.contestant_id, song_name="Voilà")
set_me_free = Song(contestant_id=eden.contestant_id, song_name="Set Me Free")
technicolour = Song(contestant_id=montaigne.contestant_id, song_name="Technicolour")
mata_hari = Song(contestant_id=efendi.contestant_id, song_name="Mata Hari")
omaga = Song(contestant_id=benny.contestant_id, song_name="omaga")
russian_woman = Song(contestant_id=manizha.contestant_id, song_name="Russian Woman")

db.session.add(amen)
db.session.add(el_diablo)
db.session.add(karma)
db.session.add(lucky_one)
db.session.add(voila)
db.session.add(set_me_free)
db.session.add(technicolour)
db.session.add(mata_hari)
db.session.add(omaga)
db.session.add(russian_woman)
db.session.commit()

blog2 = Blog(date_posted=date(2021, 4, 26),
             contestant_id=anxhela.contestant_id,
             blog_title="A little bit about Anxhela Peristeri",
             blog_text="Anxhela Peristeri was born on 24 March 1986 into an Albanian family of the Eastern Orthodox faith in the city of Korce, then part of the People's Republic of Albania, present Albania.[1][2][3] Her grandfather is of Greek origin.[4][5] After graduating from high school in Tirana, Peristeri and her family moved to Greece.[6][7] Describing her life in the latter country, she had stated that she experienced discrimination because of her Albanian origin.[8][9] In December 2001, Peristeri unsuccessfully participated in the 40th edition of Festivali i Kenges with the song 'Vetem ty te kam'.[2] Later that year, she entered the Miss Albania national pageant in Tirana.[10][11] In June 2016, she emerged as the winner of the first season of Your Face Sounds Familiar.[12] Later, in December 2016, she debuted at Kenga Magjike with the song 'Genjeshtar', finishing in the second place.[13] Then in December 2017, she won the 19th edition of Kenga Magjike with the song 'E Cmendur'.[14]",
             blog_views=0)

blog1 = Blog(date_posted=date(2021, 4, 23),
             contestant_id=vincent.contestant_id,
             blog_title="A little bit about Vincent Bueno",
             blog_text=("Bueno started dancing at the age of 4.[4] He later graduated in music and performing arts at "
                        "the Vienna Conservatory of Music. Bueno is also a composer of R&B music, having taken special "
                        "courses in acting, dancing, and singing. At age 11, he managed to play 4 musical "
                        "instruments—piano, guitar, drums, and bass guitar. His father was a former vocalist and a "
                        "1970 local band lead guitarist."),
             blog_views=0)
db.session.add(blog1)
db.session.add(blog2)
db.session.commit()

comment1 = Comment(time=datetime.utcnow(),
                   text="My first comment about Vincent Bueno",
                   blog_id=blog1.blog_id)
comment2 = Comment(time=datetime.utcnow(),
                   text="My second comment about Vincent Bueno",
                   blog_id=blog1.blog_id)
db.session.add(comment1)
db.session.add(comment2)
db.session.commit()

user1 = User(name="John", username="johndoe", password_hash=hash_password(b"password"))
db.session.add(user1)
db.session.commit()


