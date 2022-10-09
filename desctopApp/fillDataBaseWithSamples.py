from src import db, bcrypt
from src.dbmodels import Doctor, Patient, Result
from essential_generators import DocumentGenerator

db.drop_all()
db.create_all()

hash = bcrypt.generate_password_hash('test').decode('utf-8')

doc_1 = Doctor(username='dr Jan Głowala', email='test1@m.com', password=hash)
doc_2 = Doctor(username='dr Anna Matuszczak', email='test2@m.com', password=hash)

pac_1 = Patient(username='Ewelina Bratek', email='test3@m.com', password=hash, age=54)
pac_2 = Patient(username='Maciej Bartoszewski', email='test4@m.com', password=hash, age=60)
pac_3 = Patient(username='Zuzanna Borowskia', email='test5@m.com', password=hash, age=67)
pac_4 = Patient(username='Henryk Erazy', email='test6@m.com', password=hash, age=87)
pac_5 = Patient(username='Aleksandra Pohelska Erazy', email='test7@m.com', password=hash, age=46)
pac_6 = Patient(username='Adnrzej Doman', email='test8@m.com', password=hash, age=45)
pac_7 = Patient(username='Matylda Staszak', email='test9@m.com', password=hash, age=65)
pac_8 = Patient(username='Zuzanna Kołakowska', email='test10@m.com', password=hash, age=75)
pac_9 = Patient(username='Sergiusz Protazy', email='test11@m.com', password=hash, age=38)
pac_10 = Patient(username='Gerwazy Knapik', email='test12@m.com', password=hash, age=53)
pac_11 = Patient(username='Paweł Derbiusz', email='test13@m.com', password=hash, age=50)


db.session.commit()
db.session.add(doc_1)
db.session.add(doc_2)

db.session.add(pac_1)
db.session.add(pac_10)
db.session.add(pac_4)
db.session.add(pac_7)

db.session.add(pac_2)
db.session.add(pac_3)
db.session.add(pac_5)
db.session.add(pac_6)
db.session.add(pac_8)
db.session.add(pac_9)
db.session.add(pac_11)

res1 = Result(title="Zagrożenie życia", content="Analiza danych wykazuje możliwość wystąpienia zawału!", user_id=1, status=1)
res2 = Result(title="Zagrożenie życia", content="Zdrowie pacjenta uległo znacznemu pogorszeniu! Zalecana wizyta ibadania", user_id=2, status=2)
res3 = Result(title="Ostrzeżenie", content="Sugerowana wizyta kontrolna, odczyty badań pacjenta są inepokojące", user_id=3, status=3)
res4 = Result(title="Ostrzeżenie", content="Zdrowie pacjenta pogarsza się, zalecana interwencja", user_id=4, status=4)
res5 = Result(title="Uwaga", content="Odczyty wskazują na stopniowe pogarszanie się zdrowia pacjenta, zalecana wizyta kontrolna", user_id=5, status=5)
res6 = Result(title="Uwaga", content="Zdrowie pacjenta nie ulega poprawie,", user_id=6, status=6)
res7 = Result(title="Status", content="Odczyty wskazują na stopniową poprawę zdrowia pacjenta", user_id=7, status=7)
res8 = Result(title="Status", content="Wyniki analizy zdrowia pacjenta są w normach", user_id=8, status=8)
res9 = Result(title="Informacja", content="Stan zdrowia pacjenta nie wymaga interwencji", user_id=9, status=9)
res10 = Result(title="Informacja", content="Pacjent w bardzo dobrej kondycji", user_id=10, status=10)


db.session.add(res1)
db.session.add(res2)
db.session.add(res3)
db.session.add(res4)
db.session.add(res5)
db.session.add(res6)
db.session.add(res7)
db.session.add(res8)
db.session.add(res9)
db.session.add(res10)

# anno1 = Announcement(id=1, title='New version 1.0!', content='First version!')
# anno2 = Announcement(id=2, title='New version 1.1!', content='Minor update of forms and user input')
# anno3 = Announcement(id=3, title='New version 1.5!', content='Added statistics')
# anno4 = Announcement(id=4, title='New version 2.0!', content='Added map, improved time statistics, added calendar!')

db.session.commit()
