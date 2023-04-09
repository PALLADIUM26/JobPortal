#profile
import os
import mysql.connector as mc
import sys
import funcs
b=0

def pror(db,uname):
	os.system('cls')
	print('PROFILE PAGE\n')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from dataemployer where uname='%s'"%(uname,))
	record=cursor.fetchone()
	print('PERSONAL DETAILS-')
	print("USERNAME\tCOMPANY NAME\tLOCATION")
	print(record[0],'\t',record[1],'\t',record[2])
	print()
	cursor.execute("show tables;")
	f=0
	t=cursor.fetchall()
	for i in t:
		if 'jobs' in i:
			f=1
	if f==1:
		cursor.execute("select * from jobs where uname='%s'"%(uname,))
		records=cursor.fetchall()
		print('POSTED JOBS:')
		print("SERIAL NO\tUSERNAME\tJOBNAME\tCOMPANY NAME\tDESCRIPTION")
		b=1
		for i in records:
			print(b,i[0],'\t',i[1],'\t',i[2],'\t',i[3])
			b+=1
	print()
	c=input('ENTER\n1 TO EDIT DETAILS\nANY OTHER KEY TO GO BACK')
	if c=='1':
		editr(db,uname)
	else:
		return
	
def editr(db,uname):
	cursor=db.cursor()
	cursor.execute("use lj;")
	while True:
		cursor.execute("show tables;")
		f=0
		t=cursor.fetchall()
		for i in t:
			if 'jobs' in i:
				f=1
		
		if f==1:
			print('ENTER\n1 TO EDIT PERSONAL DETAILS\n2 TO EDIT POSTED JOBS\n0 TO GO BACK')
			l=['0','1','2']
		else:
			print('ENTER\n1 TO EDIT PERSONAL DETAILS\n0 TO GO BACK')
			l=['0','1']
		ch=funcs.notsame(l)
		if ch=='1':
			while True:
				print('ENTER\n1 TO EDIT MAIL ID\n2 TO EDIT PASSWORD\n3 TO EDIT LOCATION\n0 TO GO BACK')
				l1=['0','1','2','3']
				ch1=funcs.notsame(l1)
				if ch1=='1':
					m=input('Enter New Mail ID: ')
					query="update data set mail='%s' where uname='%s'"%(m,uname)
					cursor.execute(query)
					db.commit()
					print()
				elif ch1=='2':
					p=input('Enter New Password: ')
					query="update data set pwd='%s' where uname='%s'"%(p,uname)
					cursor.execute(query)
					db.commit()
					print()
				elif ch1=='3':
					loc=input('Enter New Location: ')
					query="update dataemployer set location='%s' where uname='%s'"%(loc,uname)
					cursor.execute(query)
					db.commit()
					print()
				else:
					break

		elif ch=='2':
			while True:
				cursor.execute("select * from jobs where uname='%s'"%(uname,))
				records=cursor.fetchall()
				jn=input('Enter Name of Job: ')
				print('ENTER 1 TO EDIT DESCRIPTION\t2 ELIGIBILITY\t3 FOR AGE\t0 TO GO BACK')
				l2=['0','1','2','3']
				ch2=funcs.notsame(l2)
				if ch2=='1':
					d=input('Enter new description of Job: ')
					query="update jobs set description='%s' where uname='%s'"%(d,uname)
					cursor.execute(query)
					db.commit()
					print()
				elif ch2=='2':
					e=input('Enter new Eligibility of Job: ')
					query="update jobs set eligibility='%s' where uname='%s'"%(e,uname)
					cursor.execute(query)
					db.commit()
					print()
				elif ch2=='3':
					a=input('Enter new required Age for Job: ')
					query="update jobs set age='%s' where uname='%s'"%(a,uname)
					cursor.execute(query)
					db.commit()
					print()
				else:
					break
		else:
			break
	return

	