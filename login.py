import pymysql

a= input("Enter 1 for Register and 2 for Login")
if a=="1":
	name=input("Enter Name:-")
	cnt=input("Enter Phone no.:-")
	add=input("Address:-")
	userid=input("create User ID:-")
	password=input("Creat password")
    
	db=pymysql.connect("localhost","root","Abc123@#$","akshay")
	cursor = db.cursor()
	sql= "insert into reguser values(%s,%s)"
	print(userid)

	try:
   		cursor.execute(sql,(userid,password))
   		db.commit()
   		print("DATA INSERTED")
	except:
   		db.rollback()
    


if a=="2":
	userid=input(" User ID:--")
	password=input("Password:--")
    
	db=pymysql.connect("localhost","root","Abc123@#$","akshay")
	cursor = db.cursor()
	sql= "select password from reguser where userid=%s "

	try:
   		cursor.execute(sql,(userid))
   		db.commit()
   		result = cursor.fetchone()
   		result = result[0]
	except:
		db.rollback()
		print("UserID not found   TRY AGAIN")
   		
  

if result==password:
	print("Heloo succeess")
else:
	print("Password is Wrrong")	
# COMMENT GIVE	
#some comment
