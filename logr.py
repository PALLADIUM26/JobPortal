#login 
import os
import mysql.connector as mc
import sys
import employerprofile
import funcs

def logr(db,uname):
	os.system('cls')
	print('LOGGED IN')
	print("WELCOME ",uname)
	while True:
		print('ENTER\n1 TO POST JOBS\n2 TO SEE RECEIVED APPLICATIONS\n3 GO TO PROFILE PAGE\n0 TO LOG OUT')
		ch=funcs.notsame(['1','2','3','4','0'])
		if ch=='1':
			tabr(db,uname)
		elif ch=='2':
			appr(db,uname)
		elif ch=='3':
			employerprofile.pror(db,uname)
		else:
			break
	return

def tabr(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select cname from dataemployer where uname='%s'"%(uname,))
	cname=cursor.fetchone()[0]
	jobname=input('Enter Name of Job: ')
	des=input('Enter Description of Job: ')
	elg=input('Enter Eligibility criteria (Qualifications) for Job: ')
	age=int(input('Enter required Age for Applicants: '))
	cursor.execute("create table if not exists jobs (uname varchar(30), jobname varchar(15), cname varchar(30), description varchar(100), eligibility varchar(20), age int(3));")
	query="insert into jobs (uname,jobname,cname,description,eligibility,age) values ('{}','{}','{}','{}','{}','{}')".format(uname,jobname,cname,des,elg,age)
	cursor.execute(query)
	db.commit()
	print()
	return

def appr(db,uname):
	os.system('cls')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select jobname,cname from jobs where uname='%s'"%(uname,))
	rec=cursor.fetchone()
	cursor.execute("select * from applications where jobname='%s' and cname='%s'"%(rec[0],rec[1]))
	recs=cursor.fetchall()
	l=[]
	print('SERIAL NO.\tUSERNAME\tMAIL ID\tAGE\tCONTACT\tELIGIBILITY\tEXPERIENCE\tHOBBIES\tJOB NAME\tCOMPANY NAME')
	for i in range(len(recs)):
		print(i+1,end='\t')
		print(recs[i][0],end='\t')
		print(recs[i][1],end='\t')
		print(recs[i][2],end='\t')
		print(recs[i][3],end='\t')
		print(recs[i][4],end='\t')
		print(recs[i][5],end='\t')
		print(recs[i][6],end='\t')
		print(recs[i][7],end='\t')
		print(recs[i][8],end='\t')
		print()
		l.append(str(i+1))
	while True:
		print('ENTER\n1 TO SELECT AN APPLICANT\n ANY OTHER KEY TO GO BACK')
		ch=input('Enter Your Choice: ')
		rec=0
		if ch=='1':
			print('Enter Serial Number of Applicant')
			n=funcs.notsame(l)
			for i in range(len(l)):
				if l[i]==n:
					rec=recs[i]
					break
			mail=rec[1]			
			funcs.sendmail(mail,2)
			print()
		else:
			break
	return

