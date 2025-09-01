import json
import sqlite3

conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS User')
cur.execute('DROP TABLE IF EXISTS Member')
cur.execute('DROP TABLE IF EXISTS Course')

cur.execute('CREATE TABLE User ( id INTEGER PRIMARY KEY, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Course (id INTEGER PRIMARY KEY,title  TEXT UNIQUE)')
cur.execute('CREATE TABLE Member (user_id INTEGER,course_id INTEGER,role INTEGER,PRIMARY KEY (user_id, course_id))')

fname= 'roster_data.json'
fhandle= open(fname).read()
data = json.loads(fhandle)

for line in data:

    user = line[0]
    course = line[1]
    role = line[2]
    
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(user,))
    cur.execute('SELECT id FROM User WHERE name = ?',(user,))
    user_id  = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)',(course,))
    cur.execute('SELECT id FROM Course WHERE title = ?',(course,))
    course_id  = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (course_id,user_id,role) VALUES (?,?,?)',(course_id,user_id,role))

conn.commit()

sqlcmd = '''SELECT User.name,Course.title, Member.role FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2'''

for row in cur.execute(sqlcmd):
    print(row[0],row[1],row[2])

sqlquery = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1'''

for item in cur.execute(sqlquery):
    print(item[0])

cur.close()
conn.close()
