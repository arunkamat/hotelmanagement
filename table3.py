from pymysql import *
class fo():
    def food(self):
        n=int(input("enter your choice:\n1.insert a value:\n2.update a records:\n3.delete a records:\n4.show the table"))
        if(n==1):
            try:
                sl=int(input("enter a seriel number:"))
                fn=input("enter your food name:")
                f=input("enter your flavour:")
                i=input("enter incrediants:")
                p=int(input("preperation time:"))
                ci=int(input("enter chef id:"))
                cn=input("enter chef name:")
                g=input("enter chef gender:")
                a=int(input("enter a  age:"))
                ad=input("enter a address:")
                m=int(input("enter a mobile number:"))
                st=int(input("give a stars out of 5:"))
                cm=input("enter a comments:")

                c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                q="insert into foodinfo values({0},'{1}','{2}','{3}',{4},{5},'{6}','{7}',{8},'{9}',{10},{11},'{12}')".format(sl,fn,f,i,p,ci,cn,g,a,ad,m,st,cm)
                cur=c.cursor()  
                cur.execute(q)
                c.commit()
                print("data saved")
                c.close()
    
            except Exception as e:
                print(e)
        
        elif(n==2):
            c=int(input("what do you want to update\n please enter your choice\n1.foodname\n2.flavour\n3.incrediants\n4.preperation time\n5.chef id\n6.chefname\n7.gender\n8.age\n9.address\n10.mobile\n11.stars\n12.comments"))
            if(c==1):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a food name:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set foodname='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==2):
                try:
                    n=int(input("enter a seriel no:"))
                    na=input("update a flavour:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set flavour='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==3):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a incrediants:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set incrediants='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
            elif(c==4):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a preperation time:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set preperationtime={2} where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==5):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a chef id number:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set chefid={2} where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==6):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a chef name:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set chefname='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==7):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a gender of chef:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set gender='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==8):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a age of chef:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set age={2} where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==9):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a address:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set address='{2}' where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                    
            elif(c==10):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a mobile number of chef:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set mobile={2} where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                   
            elif(c==11):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update stars for work:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set stars={2} where slno={1}".format(n,na)
                    cur=c.cursor()
                    cur.execute(q)
                    c.commit()
                    print("data updated")
                    c.close()
    
                except Exception as e:
                    print(e)
                 
            elif(c==12):
                try:
                    n=int(input("enter a seriel no:"))
               
                    na=input("update a comments:")
    
                    c=connect(host="localhost",user="root",password="",database="hotelmanagement")
                    q="update foodinfo set comments={2} where slno={1}".format(n,na)
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
                q="delete from foodinfo where slno={0}".format(s)
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
                q="select * from foodinfo"
                cur=c.cursor()
                cur.execute(q)
                c.commit()
                res=cur.fetchall()
                print("slno\tfoodname\tflavour\tincrediants\tpreperation time\tchef id\tchef name\tgender\tage\taddress\tmobile\tstars\tcomments")
                for i in res:
                    for j in i:
                        print(j,end="\t")
                    print()
                c.close()
                print("data saved")

            except Exception as e:
                print(e)
        
        else:
            print("invalid choice")
            print("only you can put number 1 to 4")