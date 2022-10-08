from src import db, bcrypt
from src.dbmodels import Doctor, Patient, Result
from essential_generators import DocumentGenerator
db.drop_all()
db.create_all()

hash = bcrypt.generate_password_hash('test').decode('utf-8')

doc_1 = Doctor(username='doc1', email='test1@m.com', password=hash)
doc_2 = Doctor(username='doc2', email='test2@m.com', password=hash)

pac_1 = Patient(username='pac1', email='test3@m.com', password=hash)
pac_2 = Patient(username='pac2', email='test4@m.com', password=hash)

res1 = Result(title="tytul 1", content="content 1")
res2 = Result(title="tytul 2", content="content 2")
res3 = Result(title="tytul 3", content="content 3")
res4 = Result(title="tytul 4", content="content 4")

db.session.add(doc_1)
db.session.add(doc_2)

db.session.add(pac_1)
db.session.add(pac_2)

db.session.add(res1)
db.session.add(res2)
db.session.add(res3)
db.session.add(res4)

# anno1 = Announcement(id=1, title='New version 1.0!', content='First version!')
# anno2 = Announcement(id=2, title='New version 1.1!', content='Minor update of forms and user input')
# anno3 = Announcement(id=3, title='New version 1.5!', content='Added statistics')
# anno4 = Announcement(id=4, title='New version 2.0!', content='Added map, improved time statistics, added calendar!')

db.session.commit()
