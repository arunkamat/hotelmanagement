from pymysql  import *
from table2 import *
from table3 import *
print("welcome to hotelmanagement profile\nyou need to login \nplease enter your username and password")
u=input("enter a user name:")
p=input("enter a password:")

c=connect(host="localhost",user="root",password="",database="hotelmanagement")
q="select * from admin"
cur=c.cursor()
cur.execute(q)
re=cur.fetchall()
for i in re:
    if(i[0]==u and i[1]==p):
        print("login successfully done")
        n=int(input("enter your choice:\n1.customer info\n2.food info\nplease enter any one...."))
        if(n==1):
            o=cus()
            o.customer()
        elif(n==2):
            o=fo()
            o.food()
            
        else:
            print("invalid choice")
    else:
        print("inavalid username or password")
        

