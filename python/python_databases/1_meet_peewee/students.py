from peewee import *

db = SqliteDatabse('students.db')

class Student(Model):
    username = CharField(max_length =225, unique=True)
    points = IntergerField(default=0)

    class Meta:
        database = db

if __name__ == '__main__':
    db.connect()
    db.create_tables(['Student'], safe=True)
