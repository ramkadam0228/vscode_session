import sqlite3

# Create a DB
conn=sqlite3.connect('example.db')
print(type(conn))
# we need to create a object
cursor=conn.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS USERS
                            (id INTEGER PRIMARY KEY,
                            name VARCHAR,
                            age INTERGER)
                            """)

# Insert  data

# cursor.execute('insert into USERS (id,name,age) VALUES (?,?,?);',(1,'Ram',30))
# cursor.execute('insert into USERS (id,name,age) VALUES (?,?,?);',(2,'Shyam',40))
# cursor.execute('insert into USERS (id,name,age) VALUES (?,?,?);',(3,'Suresh',10))

# conn.commit()

# Query
cursor.execute("select * from USERS;")
rows=cursor.fetchall()
for row in rows:
    print(row)


# cursor.execute('Update USERS set age =? where name =?',(100,'Ram'))
# cursor.execute("select * from USERS;")
# rows=cursor.fetchall()
# for row in rows:
#     print(row)


cursor.execute('delete from users where name=?',('Shyam',))
cursor.execute("select * from USERS;")
rows=cursor.fetchall()
for row in rows:
    print(row)