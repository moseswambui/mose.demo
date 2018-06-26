from initdata import mose, davy
import shelve
db=shelve.open('People-shelve')
db['mose']=mose
db['davy']=davy
db.close()

db=shelve.open('People-shelve')
for key in db:
    print(key, "=> \n", db[key])

print(db['davy']['name'])