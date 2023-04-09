#profile
import os
import mysql.connector as mc
import sys
import funcs

def proe(db,uname):
	os.system('cls')
	print('PROFILE PAGE\n')
	cursor=db.cursor()
	cursor.execute("use lj;")
	cursor.execute("select * from dataemployee where uname='%s'"%(uname,))
	record=cursor.fetchone()
	print('PERSONAL DETAILS:')
	print('USERNAME\tFATHER\'S NAME\tDATE OF BIRTH\tAGE\tCONTACT\tNATIONALITY\tADDRESS\tQUALIFICATIONS\tEXPERIENCE\tHOBBIES')
	for i in record:
		print(i,end='\t')
	print()
	c=input('ENTER\n1 TO EDIT DETAILS\nANY OTHER KEY TO GO BACK')
	if c=='1':
		edite(db,uname)
	else:
		return

def edite(db,uname):
	cursor=db.cursor()
	cursor.execute("use lj;")
	while True:
		print('ENTER 1 TO EDIT MAIL ID\t2 TO EDIT PASSWORD\t3 TO EDIT CONTACT NUMBER\t4 TO EDIT NATIONALITY\t5 TO EDIT ADDRESS\t6 TO EDIT QUALIFICATIONS\t7 TO EDIT EXPERIENCE\t8 TO EDIT HOBBIES\t0 TO GO BACK')
		l=['0','1','2','3','4','5','6','7','8']
		ch=funcs.notsame(l)
		if ch=='1':
			m=input('Enter new Mail: ')
			query="update data set mail='%s' where uname='%s'"%(m,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='2':
			p=input('Enter new password: ')
			query="update data set pwd='%s' where uname='%s'"%(p,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='3':
			cn=input('Enter new Contact no.: ')
			query="update dataemployee set cont='%s' where uname='%s'"%(cn,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='4':
			nat=input('Enter new Nationality: ')
			query="update dataemployee set nation='%s' where uname='%s'"%(nat,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='5':
			ad=input('Enter new Address: ')
			query="update dataemployee set ad='%s' where uname='%s'"%(ad,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='6':
			q=input('Enter new Qualifications: ')
			query="update dataemployee set qualf='%s' where uname='%s'"%(q,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='7':
			e=input('Enter new Experience: ')
			query="update dataemployee set exp='%s' where uname='%s'"%(e,uname)
			cursor.execute(query)
			db.commit()
			print()
		elif ch=='8':
			h=input('Enter new Hobbies: ')
			query="update dataemployee set hob='%s' where uname='%s'"%(h,uname)
			cursor.execute(query)
			db.commit()
			print()
		else:
			break
	return
