import pymysql

a= input("Enter 1 for Register")

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
	userid=input("create User ID:-")
	password=input("Creat password")
    
	db=pymysql.connect("localhost","root","Abc123@#$","akshay")
	cursor = db.cursor()
	sql= "select password from reguser where userid=%s "

	try:
   		cursor.execute(sql,(userid))
   		db.commit()
   		result = cursor.fetchone()
   		print(result)
	  #   if result==password:
			# print("Heloo succeess")
    


	except:
   		db.rollback()
  
# COMMENT GIVE	
#some comment
