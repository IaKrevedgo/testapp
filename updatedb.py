import shelve
db = shelve.open('persondb')

for key in sorted(db):
    print(key, '=>', db[key])

sue = db['Sue Jones']
sue.giveRaise(.10)                                                                              # при каждом исполнении будет накидывать sue по 10% зарплаты и сохранять в БД
db['Sue Jones'] = sue
db.close()