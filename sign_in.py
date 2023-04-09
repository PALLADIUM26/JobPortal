import funcs
import mysql.connector as mc
import sys
import funcs
import os
import loge
import logr
import admh

def sin(db):
	os.system('cls')
	flag=0
	print('**********SIGN*IN**********\n')
	print('___________________________\n')
	print('ENTER\n1 TO SIGNIN THROUGH EMAIL\n2 SIGNIN THROUGH USERNAME')
	l=['1','2']
	x,y,z,w=funcs.fetver(db)
	ch1=funcs.notsame(l)
	p=0
	mail=0
	uname=0
	typ=0
	if ch1=='1':
		mail=input('Enter Registered Email ID: ')
		while(mail not in y):
			print('UNAVAILABLE EMAIL ID!')
			mail=input('Re-Enter Registered Email ID: ')
		for i in range(len(y)):
			if mail==y[i]:
				p=z[i]
				uname=x[i]
				typ=w[i]
				break
	else:
		uname=input('Enter Registered Username: ')
		while(uname not in x):
			print('UNAVAILABLE USERNAME!')
			uname=input('Re-Enter Registered Username: ')
		for i in range(len(x)):
			if uname==x[i]:
				p=z[i]
				mail=y[i]
				typ=w[i]
				break
	pwd=input('Enter Your Password: ')

		#login
	while pwd!=p:
		print('ENTER\n1 TO RE-ENTER PASSWORD\nANY OTHER IF FORGOT PASSWORD')
		ch2=input('Enter Your Choice: ')
		if ch2=='1':
			pwd=input('Re-Enter Your Password: ')
		else:
			print('SENDING OTP TO YOUR REGISTERED MAIL-ID TO CHANGE YOUR PASSWORD')
			otp1=funcs.sendmail(mail)
			otp2=input('Enter OTP Sent in Registered Email ID: ')
			while(otp2!=otp1):
				print('ENTER\n1 TO RE-ENTER OTP\nANY OTHER KEY TO RESEND OTP')
				ch3=input('Enter Your Choice: ')
				if ch3=='1':
					otp2=input('Re-Enter OTP Sent in Registered Email ID: ')
				else:
					otp1=funcs.sendmail(mail)
					otp2=(input('Enter New OTP: '))
			print('CHANGE YOUR PASSWORD')
			pwd2=input('Enter New Password: ')
			funcs.inp(db,[uname,mail,pwd2],2)
			p=pwd2
	
	if typ=='E':
		loge.loge(db,uname)
	elif typ=='R':
		logr.logr(db,uname)
	elif typ=='A':
		admh.admh(db,uname)
	else:
		print('INVALID CHOICE!')