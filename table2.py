from pymysql import *
class cus():
    def customer(self):
        n=int(input("enter your choice:\n1.insert a value:\n2.update a records:\n3.delete a records:\n4.show the table"))
        if(n==1):
            try:
                sl=int(input("enter a seriel number:"))
                n=input("enter your name:")
                sn=input("enter your surname:")
                ad=input("enter your address:")
                p=int(input("enter a pincode:"))
                m=int(input("enter a mobile number:"))
                g=input("enter your gender:")
                cu=input("enter your oredr:")
                pr=int(input("set your price for food:"))
                di=int(input("discount for food:"))
                co=input("compliments you want:")
                st=int(input("give a stars out of 5:"))
                cm=input("enter a comments:")

                c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                q="insert into customer values({0},'{1}','{2}','{3}',{4},{5},'{6}','{7}',{8},{9},'{10}',{11},'{12}')".format(sl,n,sn,ad,p,m,g,cu,pr,di,co,st,cm)
                cur=c.cursor()  
                cur.execute(q)
                c.commit()
                print("data saved")
                c.close()
    
            except Exception as e:
                print(e)
    
        elif(n==2):
            a=int(input("what do you wants to update...\n1.name\n2.surname\n3.address\n4.pincode\n5.mobile\n6.gender\n7.customer order\n8.price\n9.discount\n10.compliment\n11.stars\n12.comments"))
            if(a==1):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a name:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set name='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
            
            elif(a==2):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a surname:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set surname='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==3):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a address:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set address='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==4):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a pincode:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set pincode={1} where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==5):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a mobile number:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set mobile={1} where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==6):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a gender:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set gender='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==7):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a customer order:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set customerorder='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(a==8):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a price:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set price={1} where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                
            elif(a==9):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a discount:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set discount={1} where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
            
            elif(a==10):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a compilments:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set compliments='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
            
            elif(a==11):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a stars for work:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set stars={1} where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
            
            elif(a==12):
                try:
                    n=int(input("enter a seriel no:"))
                    m=int(input('update a comments:'))
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update customer set comments='{1}' where slno={0}".format(n,m)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            else:
                print("invalid choice")
        elif(n==3):

            try:
                s=int(input("enter a seriel no:"))
                c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                q="delete from customer where slno={0}".format(s)
                cur=c.cursor()
                cur.execute(q)
                c.commit()
                print("data deleted")
                c.close()

            except Exception as e:
                print(e)

        elif(n==4):
            try:
                c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                q="select * from customer"
                cur=c.cursor()
                cur.execute(q)
                c.commit()
                res=cur.fetchall()
                print("slno\tname\tsurname\tstreet\tpincode\tmobile\tgender\torder\tprice\tdiscount\tcompliment\tstars\tcomments")
                for i in res:
                    for j in i:
                        print(j,end="\t")
                    print()
                c.close()
                print("data saved")

            except Exception as e:
                print(e)
    
        else:
            print("invalid input")
            print("only you can put number 1 to 4")