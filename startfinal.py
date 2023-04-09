import smtplib
import random
import os
import sys
import sign_up
import sign_in
import pickle
import mysql.connector as mc
import funcs

def strtup():#main
	os.system('cls')
	dbPWD=[]
	print('**********STARTUP**********')
	print('___________________________')
	print('~WELCOME TO LOL JOB WORLD!~\n')
	flag=0
	if os.path.isfile('DBpwd.bin')==False:
		flag=1
		print('ADMIN SIGNUP\n')
		adm=input('Enter Admin username: ')
		m=input('Enter Admin mail: ')
		p=input('Enter Admin password: ')
		l=[adm,m,p]
		print()
		uname=input("Enter Username of MYSQL: ")
		pwd=input("Enter password of MYSQL: ")
		dbPWD=[uname,pwd]
		with open('DBpwd.bin','wb+') as f:
			pickle.dump(dbPWD,f)
		f.close()
	with open('DBpwd.bin',"rb+") as f:
		dbPWD=pickle.load(f)
	f.close()
	db=mc.connect(host="localhost",user=dbPWD[0],password=dbPWD[1])
	if (db.is_connected()):
		print('DATABASE CONNECTED SUCCESSFULLY')
	if flag==1:
		funcs.inp(db,l,1)

	while(True):
		print('\nOPTIONS-')
		print('ENTER\n1: TO SIGNIN\n2: TO SIGNUP\n0: TO CLOSE')
		l=['1','2','0']
		ch=funcs.notsame(l)
		print('YOU ENTERED',ch)
		if ch!='0':
			print('REDIRECTING TO DESIRED PAGE')
		if ch=='1':	
			#open signin page
			print(1)
			sign_in.sin(db)
			os.system('cls')
		elif ch=='2':
			#open signup page
			print(2)
			sign_up.sup(db)
			os.system('cls')
		else:
			os.system('cls')
			print("EXITTED")
			db.close()
			break

#strtup()
