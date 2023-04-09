import smtplib
import random
import os
import sys
import pickle

def notsame(l):	
	ch=input('Enter Your Choice: ')
	while(ch not in l):
		print('INVALID CHOICE!')
		ch=input('Re-Enter Your Choice: ')
	return ch

def inp(db,l,t=0):
	cursor=db.cursor()
	cursor.execute("create database if not exists lj;")
	cursor.execute("use lj;")
	cursor.execute("create table if not exists data (uname varchar(30),mail varchar(30),pwd varchar(20),type char(1));")
	if t==1:
		query="insert into data (uname,mail,pwd,type) values ('{}','{}','{}','{}')".format(l[0],l[1],l[2],'A')
	elif t==2:
		query="update data set pwd='%s' where mail='%s'"%(l[2],l[1])
	else:
		query="insert into data (uname,mail,pwd,type) values ('{}','{}','{}','{}')".format(l[0],l[1],l[2],l[3])
	cursor.execute(query)
	db.commit()
	return

def fetver(db):
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from data")
	vals=cursor.fetchall()
	db1=[i[0] for i in vals]
	db2=[i[1] for i in vals]
	db3=[i[2] for i in vals]
	db4=[i[3] for i in vals]
	return db1,db2,db3,db4

def sendmail(mail,t=1):
	if t==1:
		sub='SIGNUP VERIFICATION'
		otp=str(random.randint(1000,9999))
		msg="LOL JOB WORLD\nOTP:"+otp+"\nDO NOT SHARE THIS."
		try:
			server=smtplib.SMTP("smtp.gmail.com:587")
			server.ehlo()
			server.starttls()
			server.login("kyo26sohma@gmail.com","mwfkudamcvyxsprg")
			message='Subject: {}\n\n{}'.format(sub,msg)
			server.sendmail(mail,mail,message)
			server.quit()
			print('EMAIL SENT SUCCESSFULLY!')
			return otp
		except:
			print('SOMETHING WENT WRONG!')
	else:
		sub='APLLICATION ACCEPTED'
		msg="LOL JOB WORLD\nYOU WILL BE CONTACTED SHORLY FROM COMPANY FOR INTERVIEW."
		try:
			server=smtplib.SMTP("smtp.gmail.com:587")
			server.ehlo()
			server.starttls()
			server.login("kyo26sohma@gmail.com","mwfkudamcvyxsprg")
			message='Subject: {}\n\n{}'.format(sub,msg)
			server.sendmail(mail,mail,message)
			server.quit()
			print('EMAIL SENT SUCCESSFULLY!')
		except:
			print('SOMETHING WENT WRONG!')
