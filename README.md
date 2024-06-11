# JobPortal
 - Basic CUI based Job Portal
 - Made using `Python`
 - `MySQL` was used for DBMS.

For proper functioning of this, you must have Python and MySQL installed in your systems. Especially `mysql.connector`, `pickle` and `smtplib` packages of python are used.

<br>

## Commands for starting:
 - `pip install mysql-connector-python`
 - `pip install secure-smtplib`
 - pickle is pre-installed
 - Run the <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/Main.py">Main.py</a> file by `py Main.py`

<br>

## Description:
 - Here you can sign up and sign in as Employer and Employee for different uses.
 - There is also place for Admin to maintain the portal and databases.
 - While running for first time, the ADMIN will be asked to enter the credentials of the MySQL.
 - Enter the correct credentials for smooth functioning.

<br>

## Functionalities added for both Employers, Employees and Admins:
 - While signing up there will be otp verification.
 - Employers will be able to post jobs and accept applocations.
 - Employees can search for jobs and apply.
 - Users can update their account too.

<br>

## Contents of files:
### 1. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/Main.py">Main.py</a>
 - Calls `strtup()` function from `startfinal.py`
### 2. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/startfinal.py">startfinal.py</a>
 - Creates `binary file`
 - For first time run in local system
   - Admin enters his credentials 
   - Admin enters username and password for database
 - Database login details are stored in a binary file
 - Unpickles binary file to read credentials of database
 - Connects database
 - Redirect to Sign up/ Sign in page
### 3. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/sign_up.py">sign_up.py</a>
 - #### sup()
   - Takes user credentials as input
   - Sends `OTP` to entered mail id for verification
   - Stores user credentials in database
 - #### super()
   - Takes details of Employer as input
 - #### signupEmployer()
   - Stores entered details of Employer
 - #### supee()
   - Takes details of Employee as input
   - Stores entered details of Employee in database
### 4. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/sign_in.py">sign_in.py</a>
 - #### sin()
   - Signs in user if correct credentials are entered
   - Allows to change password if forgotten by user by email verification
### 5. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/loge.py">loge.py</a>
 - #### loge()
 - #### tabe()
 - #### tabeall()
### 6. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/logr.py">logr.py</a>
 - #### logr()
 - #### tabr()
 - #### appr()
### 7. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/admh.py">admh.py</a>
 - #### admh()
 - #### admdet()
 - #### showdata()
### 8. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/funcs.py">funcs.py</a>
 - #### notsame()
 - #### inp()
 - #### fetver()
 - #### sendmail()
### 9. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/employerprofile.py">employerprofile.py</a>
 - #### pror()
 - #### editr()
### 10. <a href="https://github.com/PALLADIUM26/JobPortal/blob/main/employeeprofile.py">employeeprofile.py</a>
 - #### proe()
 - #### edite()

<br>

This project is not complete and still needs to add more functionalities and make it better.

Thank You.
