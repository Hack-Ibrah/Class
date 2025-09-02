# SQLite demo by Hack-Ibrah
import sqlite3
conn = sqlite3.connect('school.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, course TEXT)')
c.execute('INSERT INTO students (name, course) VALUES (?,?)', ('Hack-Ibrah','Software Development'))
conn.commit()
c.execute('SELECT * FROM students')
print(c.fetchall())
conn.close()
