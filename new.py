from flask import Flask, render_template,request,redirect,url_for,send_file
import exam
import random
import mysql.connector
import Sadguru
import mailer
# import datetime
app = Flask(__name__)
# 0=loginvalidation 1=loginmail
list=['No','mail','Exam sub',0]
Rollno=[]
print(list)
question=0
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="6174@Adarsha",
    database="adarsha")
cursor = db.cursor()
@app.route('/signout')
def Signout():
    list[0]='No'
    list[1]='mail'
    return render_template('choose.html')
@app.route('/')
def Root():
    return render_template('choose.html')
@app.route('/choose',methods=['POST'])
def choose():
    if request.method=='POST':
        if request.form['type']=='Lecturer':
            return render_template('Lecturerlogin.html')
        elif request.form['type']=='Student':
            return render_template('Studentlogin.html')
@app.route('/forgot',methods=['GET', 'POST'])
def forgot():
    return render_template('forgot.html')
@app.route('/Slogin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # print(list)
        cursor = db.cursor()
        username = request.form['username']
        password = request.form['password']
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM login WHERE mail_id=%s AND password=%s", (username, password))
        user=cursor.fetchone()
        # Rollno.append(user[2])
        # print(user)
        cursor.close()
        if user:
            list[1]=username
            list[0]='Yes'
            Rollno.append(user[2])
            print(user)
            return redirect('/Shome')
        else:
            return render_template('Studentlogin.html', message="Invalid credentials. Please try again.")

    return render_template('Studentlogin.html')
Lecturer=['No','a']
@app.route('/Llogin', methods=['GET', 'POST'])
def Llogin():
    if request.method == 'POST':
        cursor = db.cursor()
        username = request.form['username']
        password = request.form['password']
        # Check if the user exists in the database
        cursor.execute("SELECT * FROM Llogin WHERE mail=%s AND password=%s", (username, password))
        user=cursor.fetchone()
        print(user)
        cursor.close()
        if user:
            Lecturer[1]=username
            Lecturer[0]='Yes'
            return render_template('Lhome.html',Quote=Sadguru.one[0]['quote'])
        else:
            return render_template('Lecturerlogin.html', message="Invalid credentials. Please try again.")

    return render_template('Studentlogin.html')
@app.route('/Lhome')
def Lhome():
    return render_template('Lhome.html')
@app.route('/roll',methods=['GET','POST'])
def Roll():
    if request.method=='POST':
        roll=request.form['roll']
        print(roll)
        cursor.execute('select * from details where roll_number=%s',[roll])
        Details=cursor.fetchone()
        if Details:
            return render_template('StudentDetails.html',a=Details)
        else:
            return render_template('Roll.html',data='Invalid Roll Number')

    return render_template('Roll.html')
# @app.route('/details',methods=['POST','GET'])
# def Details():
#     return render_template('StudentDetails.html')

@app.route('/Shome')
def home():
        # Check if the user is authenticated using the session
    if 'Yes' in list:
        return render_template('Shome.html',Quote=Sadguru.one[0]['quote'])
    else:
        return redirect('/Slogin')




@app.route('/Select')
def Select():
        # Check if the user is authenticated using the session
    if 'Yes' in list:
        return render_template('select.html')
    else:
        return redirect('/login')
# Qno=0
@app.route('/Exam',methods=['GET', 'POST'])
def Exam():
    if request.method=='POST':
        if request.form['option']=='1':
            list[2]=request.form['option']
            list[3]=0
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.c[0]['question'],Option=exam.c[0]['options'],roll=list[1].upper(),sub=0,ans=20,ex_name='C Programming')
        elif request.form['option']=='2':
            list[2]=request.form['option']
            list[3]=0
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.sc[0]['question'],Option=exam.sc[0]['options'],roll=list[1].upper(),sub=0,ans=20,ex_name='Java Script')
        elif request.form['option']=='3':
            list[2]=request.form['option']
            list[3]=0
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.java[0]['question'],Option=exam.java[0]['options'],roll=list[1].upper(),sub=0,ans=20,ex_name='Java')
        elif request.form['option']=='4':
            list[2]=request.form['option']
            list[3]=0
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.a[0]['question'],Option=exam.a[0]['options'],roll=list[1].upper(),sub=0,ans=20,ex_name='Python')
@app.route('/next',methods=['GET','POST'])
def Next():
    if list[3]!=(len(exam.c)-1) and (len(exam.sc)-1) and (len(exam.java)-1):
        list[3]=list[3]+1
    if list[2]=='1':
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.c[list[3]]['question'],Option=exam.c[list[3]]['options'],roll=list[1].upper(),sub=20-(cmarks.count(0)),ans=cmarks.count(0),ex_name='C Programming')
    elif list[2]=='2':
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.sc[list[3]]['question'],Option=exam.sc[list[3]]['options'],roll=list[1].upper(),sub=20-(scmarks.count(0)),ans=scmarks.count(0),ex_name='Java Script')
    elif list[2]=='3':
            return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.java[list[3]]['question'],Option=exam.java[list[3]]['options'],roll=list[1].upper(),sub=20-(jmarks.count(0)),ans=jmarks.count(0),ex_name='Java')
    elif list[2]=='4':
        return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.a[list[3]]['question'],Option=exam.a[list[3]]['options'],roll=list[1].upper(),sub=20-(pmarks.count(0)),ans=pmarks.count(0),ex_name='Python')
    return redirect('/next')
@app.route('/pre',methods=['GET'])
def Pre():
    list[3]=list[3]-1
    if list[2]=='1':
        return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.c[list[3]]['question'],Option=exam.c[list[3]]['options'],roll=list[1].upper(),sub=20-(cmarks.count(0)),ans=cmarks.count(0),ex_name='C Programming')
    elif list[2]=='2':
        return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.sc[list[3]]['question'],Option=exam.sc[list[3]]['options'],roll=list[1].upper(),sub=20-(scmarks.count(0)),ans=scmarks.count(0),ex_name='Java Script')
    elif list[2]=='3':
        return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.java[list[3]]['question'],Option=exam.java[list[3]]['options'],roll=list[1].upper(),sub=20-(jmarks.count(0)),ans=jmarks.count(0),ex_name='Java')
    elif list[2]=='4':
        return render_template('exam.html',Q=list[3],Num=list[3]+1,Question=exam.a[list[3]]['question'],Option=exam.a[list[3]]['options'],roll=list[1].upper(),sub=20-(pmarks.count(0)),ans=pmarks.count(0),ex_name='Python')
        
cmarks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
jmarks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
scmarks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
pmarks=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
@app.route('/score',methods=['GET', 'POST'])
def Score():
    if request.method=='POST':
        ans=request.form['ans']
        if list[2]=='1':
            cmarks[int(ans[1:])]=ans[0]
        elif list[2]=='2':
            scmarks[int(ans[1:])]=ans[0]
        elif list[2]=='3':
            jmarks[int(ans[1:])]=ans[0]
        elif list[2]=='4':
            pmarks[int(ans[1:])]=ans[0]
        print(scmarks)
        return redirect('/next')
Date=[0]
@app.route('/branch',methods=['POST','GET'])
def Branch():
    if request.method=='POST':
        cursor=db.cursor()
        branch=request.form['type']
        Date[0]=request.form['date']
        cursor.execute("SELECT roll_number,student_name FROM students where branch=%s",[branch])
        data=cursor.fetchall()
        # print(data)
        cursor.close()
        return render_template('attendence2.html',data=data)
    return render_template('Branch.html')
@app.route('/result')
def Result():
    return render_template('Results.html',Roll=Rollno[0])
OTP=[]
@app.route('/mail',methods=['POST','GET'])
def Mail():
    if request.method=='POST':
        user_mail=request.form['mail']
        cursor=db.cursor()
        cursor.execute('select mail_id from details where mail_id=%s',[user_mail])
        mail=cursor.fetchall()
        cursor.close()
        if mail:
            otp=random.randint(111111,999999)
            OTP.append(otp)
            OTP.append(user_mail)
            message=f'Your OTP for changing password for student login is {otp}'
            mailer.SendMail(user_mail,message)
            return render_template('forgot.html')
        else: 
            return render_template('mail.html',data='Please enter valid Mail_Id')
    return render_template('mail.html')
@app.route('/changepassword',methods=['POST'])
def changePassword():
    if request.method=='POST':
        password=request.form['password']
        otp=request.form['otp']
        cursor=db.cursor()
        if str(OTP[0])==otp:
            cursor.execute('update login set password=%s where mail_id=%s',[password,OTP[1]])
            db.commit()
            cursor.close()
            return redirect('/Slogin')
        else:
            return render_template('forgot.html',message='Wrong OTP entered')
print(Date)
@app.route('/postattendence',methods=['POST','GET'])
def postattendence():
    if request.method=='POST':
        cursor=db.cursor()
        date=Date[0]
        date=date.split('-')
        date='_'.join(date)
        # Check if the column exists
        column_query = 'SELECT COUNT(*) FROM information_schema.columns WHERE table_name = %s AND column_name = %s'
        cursor.execute(column_query,['register',date])
        column_exists = cursor.fetchone()[0]

        if column_exists == 0:
            # Add the column
            cursor.execute(f'alter table register add column {date} varchar(10) default "Absent"')
        Roll=[]
        present='Present'
        for i in request.form:
            Roll.append(i)
        for i in Roll:
            query=f'update register set {date} = "{present}" where roll_number = "{i}"'
            cursor.execute(query)
            db.commit()
        cursor.close()
    return redirect('/Lhome')
@app.route('/register')
def Register():
    cursor=db.cursor()
    cursor.execute('select * from register where mail_id=%s',[list[1]])
    data=cursor.fetchall()
    present=data[0][2:]
    p=present.count('Present')
    ab=present.count('Absent')
    total=p+ab
    status=[p,ab]
    cursor.execute('desc register')
    columns=[column[0] for column in cursor.fetchall()]
    column=columns[2:]
    comp=[]
    pre=(p/total)*100
    perab=(ab/total)*100
    if pre>=75:
        message='Keep it up,good attendence'
    else:
        message='Need to improve your attendence'
    conic=f'conic-gradient(orange {pre}%,yellow {perab}% );'
    for i in range(len(column)):
        comp.append((column[i],present[i]))
    cursor.close()
    return render_template('attendence_register.html',comp=comp,conic=conic,message=message)
@app.route('/finish')
def Finish():
    if list[2]=='1':
        score=exam.result(list[2],cmarks)
    elif list[2]=='2':
        score=exam.result(list[2],scmarks)
    elif list[2]=='3':
        score=exam.result(list[2],jmarks)
    elif list[2]=='4':
        score=exam.result(list[2],pmarks)
    return f"{score}"


        

if __name__=='__main__':
    app.run()
