import sqlite3

class Data:
    conn = sqlite3.connect("Data.db")
    c = conn.cursor()

    def create(self):
        Data.c.execute("CREATE TABLE IF NOT EXISTS stud(name TEXT,sec TEXT)")

    def insert(self):
        Data.c.execute("insert into stud values('anshu','c')")
        Data.c.execute("insert into stud values('ravi','c')")
        Data.c.execute("insert into stud values('rohit','b')")
        Data.conn.commit()

    def read(self):
        Data.c.execute('select * from stud')
        for i in Data.c.fetchall():
            print(i)


obj=Data()
obj.create()
obj.insert()
obj.read()
