import mysql.connector
semail=[]
# semail.append('20kq1a05a9@pace.ac.in')
a='20kq1a05a9@pace.ac.in'
# semail.append("6174@Adarsha")
# print(semail)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6174@Adarsha",
    database="adarsha")
cursor = db.cursor()
cursor.execute('select * from submit')
cursor.fetchone()
# print(a)
# B=cursor.execute('SELECT * FROM submit WHERE email= %s ',(a))
# #email=cursor.fetchone()
# print(B)
cursor.execute("SELECT * FROM submit WHERE email=%s ", [a])
user=cursor.fetchone()
print(user)