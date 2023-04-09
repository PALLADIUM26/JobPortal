import mysql.connector as mc
import os
import sys
import funcs

def admh(db,uname):
	os.system('cls')
	print('LOGGED IN')
	print("WELCOME ",uname)
	while True:
		print('ENTER \n1 TO SEE OR EDIT DETAILS \n2 ADD NEW ADMIN \n3 TO SHOW DATABASES \n0 TO LOG OUT')
		ch=funcs.notsame(['1','2','3','0'])
		if ch=='1':
			admdet(db,uname)
		elif ch=='2':
			os.system('cls')
			uname=input('Enter Admin Username: ')
			mail=input('Enter Mail Id of new Admin: ')
			pwd=input('Enter password: ')
			l=[uname,mail,pwd]
			funcs.inp(db,l,1)
		elif ch=='3':
			showdata(db,uname)
		else:
			break

def admdet(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from data where uname='%s'"%(uname,))
	rec=cursor.fetchone()
	ch=input('ENTER 1 TO EDIT DETAILS \t ANY OTHER KEY TO GO BACK: ')
	if ch=='1':
		print('ENTER 1 TO EDIT ADMIN NAME \t2 TO EDIT EMAIL ID \t3 TO EDIT PASSWORD')
		l=['1','2','3']
		ch=funcs.notsame(l)
		if ch=='1':
			un=input('Enter New Username: ')
			cursor.execute("update data set uname='%s' where uname='%s'"%(un,uname))
			db.commit()
		elif ch=='2':
			ml=input('Enter New Email Id: ')
			cursor.execute("update data set mail='%s' where uname='%s'"%(ml,uname))
			db.commit()
		else:
			pwd=input('Enter New password: ')
			cursor.execute("update data set pwd='%s' where uname='%s'"%(pwd,uname))
			db.commit()
	else:
		return

def showdata(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("show tables;")
	tab=cursor.fetchall()
	f1=f2=f3=f4=0
	for i in tab:
		if i[0]=='dataemployer':
			f1=1
		elif i[0]=='dataemployee':
			f2=2
		elif i[0]=='jobs':
			f3=3
		elif i[0]=='applications':
			f4=4

	print('ENTER 1 TO SEE ALL TABLES \t2 TO SEE ALL CUSTOMERS \t3 TO SEE EMPLOYERS \t4 TO SEE EMPLOYEES \t5 TO SEE POSTED JOBS \t6 TO SEE SUBMITTED APPLICATIONS \tANY OTHER KEY TO GO BACK-')
	while True:
		ch=input('Enter Choice: ')
		if ch=='1':
			print('ALL TABLES')
			cursor.execute("SHOW TABLES;")
			b=cursor.fetchall()
			for i in b:
				print(i[0])
			print()

			print('ALL CUSTOMERS')
			print('USERNAME\tMAIL ID\tPASSWORD\tTYPE')
			cursor.execute('select * from data;')
			a=cursor.fetchall()
			for i in a:
				for j in i:
					print(j,end='\t')
				print()
			print()

			if f1==1:
				print('ALL EMPLOYERS')
				print('USERNAME\tCOMPANY NAME\tLOCATION')
				cursor.execute('select * from dataemployer;')
				c=cursor.fetchall()
				for i in c:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR EMPLOYERS')

			if f2==2:
				print('ALL EMPLOYEES')
				print('USERNAME\tFATHER\'S NAME\tDATE OF BIRTH\tAGE\tCONTACT\tNATIONALITY\tADDRESS\tQUALIFICATIONS\tEXPERIENCE\tHOBBIES')
				cursor.execute('select * from dataemployee;')
				d=cursor.fetchall()
				for i in d:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR EMPLOYEES')

			if f3==3:
				print('POSTED JOBS')
				print('USERNAME\tJOB NAME\tCOMPANY NAME\tDESCRIPTION\tELIGIBILITY\tREQUIRED AGE')
				cursor.execute('select * from jobs;')
				e=cursor.fetchall()
				for i in e:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR POSTED JOBS')	

			if f4==4:
				print('SUBMITTED APPLICATIONS')
				print('USERNAME\tMAIL ID\tAGE\tCONTACT\tELIGIBILITY\tEXPERIENCE\tHOBBIES\tJOB NAME\tCOMPANY NAME')
				cursor.execute('select * from applications;')
				f=cursor.fetchall()
				for i in f:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR SUBMITTED APPLICATIONS')

		elif ch=='2':
			print('ALL TABLES')
			cursor.execute("SHOW TABLES;")
			b=cursor.fetchall()
			for i in b:
				print(i)
			print()

			print('ALL CUSTOMERS')
			print('USERNAME\tMAIL ID\tPASSWORD\tTYPE')
			cursor.execute('select * from data;')
			a=cursor.fetchall()
			for i in a:
				for j in i:
					print(j,end='\t')
				print()
			print()

		elif ch=='3':
			if f1==1:
				print('ALL EMPLOYERS')
				print('USERNAME\tCOMPANY NAME\tLOCATION')
				cursor.execute('select * from dataemployee;')
				c=cursor.fetchall()
				for i in c:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR EMPLOYERS')

		elif ch=='4':
			if f2==2:
				print('ALL EMPLOYEES')
				print('USERNAME\tFATHER\'S NAME\tDATE OF BIRTH\tAGE\tCONTACT\tNATIONALITY\tADDRESS\tQUALIFICATIONS\tEXPERIENCE\tHOBBIES')
				cursor.execute('select * from dataemployer;')
				d=cursor.fetchall()
				for i in d:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR EMPLOYEES')

		elif ch=='5':
			if f3==3:
				print('POSTED JOBS')
				print('USERNAME\tJOB NAME\tCOMPANY NAME\tDESCRIPTION\tELIGIBILITY\tREQUIRED AGE')
				cursor.execute('select * from jobs;')
				e=cursor.fetchall()
				for i in e:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR POSTED JOBS')

		elif ch=='6':
			if f4==4:
				print('SUBMITTED APPLICATIONS')
				print('USERNAME\tMAIL ID\tAGE\tCONTACT\tELIGIBILITY\tEXPERIENCE\tHOBBIES\tJOB NAME\tCOMPANY NAME')
				cursor.execute('select * from applications;')
				f=cursor.fetchall()
				for i in f:
					for j in i:
						print(j,end='\t')
					print()
				print()
			else:
				print('NO DATA AVAILABLE FOR SUBMITTED APPLICATIONS')

		else:	
			break
	return