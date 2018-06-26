import pprint
mose={'name':'Moses Ndungu', 'age':21, 'pay':45000, 'job':'blackhat'}
davy={'name':'David Mwangi', 'age':22, 'pay':40000, 'job':'designer'}
denno={'name':'Dennis Kamau', 'age':21, 'pay':40000, 'job':'android developer'}

db={}
db['mose']=mose
db['davy']=davy
db['denno']=denno

if __name__=='__main__':
    for key in db:
        print(key, '=>\n', db[key])