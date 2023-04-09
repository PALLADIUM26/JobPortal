#login 
import os
import sys
import funcs
import mysql.connector as mc
import employeeprofile

def loge(db,uname):
	os.system('cls')
	print('LOGGED IN')
	print("WELCOME ",uname)
	while True:
		print('ENTER\n1 SEARCH JOBS\n2 SEARCH JOBS FOR ALL\n3 GO TO PROFILE PAGE\n0 TO LOG OUT')
		ch=funcs.notsame(['1','2','3','0'])
		if ch=='1':
			tabe(db,uname)
		elif ch=='2':
			tabeall(db,uname)
		elif ch=='3':
			employeeprofile.proe(db,uname)
		else:
			break
	return

def tabe(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from data where uname='%s'"%(uname,))
	val1=cursor.fetchone()
	cursor.execute("select * from dataemployee where uname='%s'"%(uname,))
	val2=cursor.fetchone()
	cursor.execute("select * from jobs;")
	records=cursor.fetchall()
	l=[]
	print('SERIAL NO.\tUSERNAME\tJOBNAME\tCOMPANY NAME\tDESCRIPTION\tELIGIBILITY\tAGE')
	for i in range(len(records)):
		if records[i][4] in val2[7]:
			print(i+1,end='\t')
			print(records[i][0],end='\t')
			print(records[i][1],end='\t')
			print(records[i][2],end='\t')
			print(records[i][3],end='\t')
			print(records[i][4],end='\t')
			print(records[i][5],end='\t')
			l.append(str(i+1))
			print()
	while True:
		print('ENTER\n1 TO APPLY FOR A JOB\nANY OTHER KEY TO GO BACK')
		ch=input('Enter Your Choice: ')
		if ch=='1':
			print('Enter Serial Number of Job')
			jobapp=funcs.notsame(l)
			for i in range(len(records)):
				if int(jobapp)-1==i:
					val=records[i]
					break
			cursor.execute("select jobname,cname from jobs where jobname='%s'"%(val[1],))
			rec2=cursor.fetchone()		
			cursor.execute("create table if not exists applications (uname varchar(30),mail varchar(30),age int(3),cont bigint(20),eligibility varchar(20),exp varchar(30),hob varchar(30), jobname varchar(15), cname varchar(30));")
			query="insert into applications (uname,mail,age,cont,eligibility,exp,hob, jobname, cname) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(uname,val1[1] ,val2[3],val2[4],val2[7],val2[8],val2[9],rec2[0],rec2[1])
			cursor.execute(query)
			db.commit()
			print()
		else:
			break
	return

def tabeall(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from jobs;")
	records=cursor.fetchall()
	l=[]
	val=0
	print('SERIAL NO.\tUSERNAME\tJOBNAME\tCOMPANY NAME\tDESCRIPTION\tELIGIBILITY\tAGE')
	for i in range(len(records)):
		print(i+1,end='\t')
		print(records[i][0],end='\t')
		print(records[i][1],end='\t')
		print(records[i][2],end='\t')
		print(records[i][3],end='\t')
		print(records[i][4],end='\t')
		print(records[i][5],end='\t')
		print()
		l.append(str(i+1))
	while True:
		print('ENTER\n1 TO APPLY FOR A JOB\nANY OTHER KEY TO GO BACK')
		ch=input('Enter Your Choice: ')
		if ch=='1':
			jobapp=funcs.notsame(l)
			for i in range(len(records)):
				if int(jobapp)-1==i:
					val=records[i]
					break
			cursor.execute("select * from dataemployee where uname='%s'"%(uname,))
			rec1=cursor.fetchone()
			cursor.execute("select jobname,cname from jobs where jobname='%s'"%(val[1],))
			rec2=cursor.fetchone()
			cursor.execute("select * from data where uname='%s'"%(uname,))
			mail=cursor.fetchone()
			cursor.execute("create table if not exists applications (uname varchar(30),mail varchar(30),age int(3),cont bigint(20),eligibility varchar(20),exp varchar(30),hob varchar(30), jobname varchar(15), cname varchar(30));")
			query="insert into applications (uname,mail,age,cont,eligibility,exp,hob, jobname, cname) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(uname,mail[1] ,rec1[3],rec1[4],rec1[7],rec1[8],rec1[9],rec2[0],rec2[1])
			#query="insert into applications (mail)values ('{}')".format(mail[1])
			#query="insert into applications (uname,age,cont,eligibility,exp,hob) values ('{}','{}','{}','{}','{}','{}')".format(uname,rec1[3],rec1[4],rec1[7],rec1[8],rec1[9])
			#query="insert into applications (jobname,cname) values ('{}','{}')".format(rec2[0],rec2[1])
			cursor.execute(query)
			db.commit()
			print()
		else:
			break
	return
