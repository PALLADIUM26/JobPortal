import datetime
import mysql.connector as mc
import sys
import funcs
import os

def sup(db):
	os.system('cls')
	print('**********SIGN*UP**********')
	print('___________________________\n')
	u,m,p,t=funcs.fetver(db)
	print('ENTER USER TYPE')
	print('ENTER\t\'R\' FOR  EMPLOYER\t|\t\'E\' FOR EMPLOYEE')
	l=['e','E','R','r']
	typ=funcs.notsame(l)
	typ=typ.upper()
	print('IF ENTERED WRONG RESPONSE ENTER # TO RE-ENTER')
	uname=input('Enter Username: ')
	if uname=='#':
		return
	while(uname in u):
		print('ENTERED USERNAME ALREADY IN USE!')
		uname=input('Enter Another Username: ')
	mail=input('Enter Valid Email ID: ')
	if mail=='#':
		return
	while(mail in m):
		print('ENTERED EMAIL ID ALREADY IN USE!')
		mail=input('Enter Another Valid Email ID: ')
	pwd1=input('Enter Password: ')
	if pwd1=='#':
		return
	pwd2=input('Re-Enter Password: ')
	while(pwd1!=pwd2):
		print('WRONG PASSWORD!')
		pwd2=input('Re-Enter Password: ')

	otp1=funcs.sendmail(mail)
	otp2=input('Enter OTP Sent in Provided Email ID: ')
	while(otp2!=otp1):
		print('ENTER\t1 TO RE-ENTER OTP\tANY OTHER KEY TO RESEND OTP')
		ch=input('Enter Your Choice: ')
		if ch=='1':
			otp2=input('Re-Enter OTP Sent in Provided Email ID: ')
		else:
			otp1=funcs.sendmail(mail)
			otp2=(input('Enter New OTP: '))
	l=[uname,mail,pwd2,typ]
	funcs.inp(db,l)
	if typ=='E':
		supee(db,uname)
	else:
		super(db,uname)
	return

def super(db,uname):
	os.system('cls')
	print('DETAILS FOR EMPLOYER\n')
	cname=input('Enter Company\'s Name: ')
	loc=input('Enter Location: ')
	signupEmployer(db,uname,cname,loc)
	return

def signupEmployer(db,uname,cname,loc):
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("create table if not exists dataEmployer (uname varchar(30),cname varchar(30),location varchar(100));")
	query="insert into dataEmployer (uname,cname,location) values ('{}','{}','{}')".format(uname,cname,loc)
	cursor.execute(query)
	db.commit()
	return

def supee(db,uname):
	os.system('cls')
	print('DETAILS FOR EMPLOYEE\n')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("create table if not exists dataEmployee (uname varchar(30),fname varchar(30),dob date,age int(3),cont bigint(20),nation varchar(30),ad varchar(30),qualf varchar(30),exp varchar(30),hob varchar(30));")
	fname=input('Enter Father\'s Name: ')
	print('Enter Date of Birth:')
	d1=int(input('\tBirth Date(dd)- '))
	d2=int(input('\tBirth Month(mm)- '))
	d3=int(input('\tBirth Year(yyyy)- '))
	age=int(input('Enter Age: '))
	#age=
	cont=int(input('Enter Contact Number: '))
	nation=input('Enter Nationality: ')
	ad=input('Enter Address: ')
	qualf=input('Enter Educational Qualifications: ')
	exp=input('Enter WORK EXPERIENCE: ')
	hob=input('Enter Hobbies or Skills: ')
	dob=datetime.date(d3,d2,d1)
	query="insert into dataEmployee (uname,fname,dob,age,cont,nation,ad,qualf,exp,hob) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(uname,fname,dob,age,cont,nation,ad,qualf,exp,hob)
	cursor.execute(query)
	db.commit()
	return

