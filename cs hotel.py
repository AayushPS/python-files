import mysql.connector as m
import time
conn=m.connect(host='localhost',user='root',passwd='190404')
xyz=0



if conn.is_connected():
    co=conn.cursor()

    def executer(s):
        co.execute(s)
    
    def allfetcher():
        return co.fetchall()

    def reg_staff():    
        s_name=input("Enter staff member's name : ")
        s_ph=int(input("Enter staff member's phone number : "))
        s_add=input("Enter staff member's permanent residential address : ")
        s_email=input("Enter email id : ")
        s_pos=input("Enter his/her job : ")
        s_salary=int(input("Salary : "))
        s_floor_allotted=int(input("Enter floor allotted to staff member : "))
        id_operator()
        executer('select * from counter1;')
        check=allfetcher()
        sid="S"+str(len(check))
        m="insert into staff"+ "(st_id,st_name,st_address,st_phno,st_emailid,st_job,st_salary,st_floor) values ('{}','{}','{}',{},'{}','{}',{},{})".format(sid,s_name,s_add,s_ph,s_email,s_pos,s_salary,s_floor_allotted)
        executer(m)
        conn.commit()
        print("\nStaff member added successfully")
        time.sleep(1)
        
    def id_operator():
        s="create table if not exists counter1(cd varchar(5) not null);"   ###
        executer(s)
        j="insert into counter1(cd) values('{}')".format('ok')
        executer(j)
        conn.commit()

    def cust_details(floor,roomtype):
        c_name=input("Enter name : ")
        c_add=input("Enter address : ")
        c_ph=int(input("Enter phone number : "))
        c_email=input("Enter email address : ")
        c_date=input("Enter Check in Date in format yyyy-mm-dd : ")
        stayingdate=int(input("Enter no. of days you wish to stay : "))
        r_type=roomtype
        rno=int(floor[5:])*10 +c-2+(r_type*2)
        executer("select * from "+floor+" where room_no="+str(rno)+";")
        if len(allfetcher())==0:
            pass
        else:
            rno=rno-1
        m="insert into "+ floor +"(room_no, cust_name ,cust_address , ph_no,c_email ,room_type,Check_in_date,Day_duration) values ({},'{}','{}',{},'{}',{},'{}',{})".format(rno,c_name,c_add,c_ph,c_email,r_type,c_date,stayingdate)
        executer(m)
        conn.commit()    ####
        print()
        print("Your Room No. : ",rno)
        print()
        print("ROOM BOOKED SUCCESSFULLY !!!")
        time.sleep(1.5)

    def cust_details_output():
        print("~"*90)
        print("How you want to access data?")
        print("1. Whole at once")
        print("2. floor wise")
        print()
        os=int(input("How you want to access data? "))
        print()
        print()
        s="select * from floor"
        if os==1:
            data_found=0
            for i in range(1,i_ques2+1):                
                k=str(i)
                j=s+k
                executer(j)
                d=allfetcher()
                if len(d)==0:
                    pass
                else:
                    data_found=1
                    print("• This is the data for FLOOR"+k)
                    print("Room no., Customer name, Customer address, Phone no., Customer email, Room Type, Check in date, No. of days booked for")
                    for on in d:
                        print('→',on)
                    print()
            if data_found==0:
                time.sleep(0.35)
                print("NO DATA FOUND")
        elif os==2:
            d=str(int(input("For what floor you want to access data? ")))
            print()
            d=s+d
            executer(d)
            e=allfetcher()
            if len(e)==0:
                print("There's no room booked at this floor right now.")
            else:
                print("Room no., Customer name, Customer address, Phone no., Customer email, Room Type, Check in date, No. of days booked for")
                for on in e:
                    print('→',on)
                print()
        else:
            print("Wrong input!\nGoing back to Main Menu........")
        time.sleep(1.5)
        input("Press Enter to Continue.......")

    def staffdetailer():
        print("~"*90)
        print("How you want to access data?")
        print("1. Whole at once")
        print("2. floor wise")
        print()
        os=int(input("How you want to access data? "))
        print()
        print()
        if os==1:
            print()
            executer("select * from staff")
            pr=allfetcher()
            if len(pr)==0:
                time.sleep(0.35)
                print("No data found")
            print("These are details of your staff")
            print("id, Name, Address, Phone no., Email id, Job, Salary, Floor alloted")
            for i in pr:
                print(i)
        elif os==2:
            print()
            llll=str(int(input("For which floor you would like to fetch data? : ")))
            executer("select st_id, st_name, st_address, st_phno, st_emailid, st_job, st_salary from staff where st_floor="+llll+';')
            pr=allfetcher()
            print("These are details of your staff which works on floor number "+llll)
            print("id, Name, Address, Phone no., Email id, Job, Salary")
            for i in pr:
                print(i)
        time.sleep(1.5)
        input("Press Enter to Continue.......")


    def checkout():
        executer("create table if not exists past_visitors(cust_name varchar(20) not null ,cust_address longtext not null, ph_no bigint(20) not null unique, c_email varchar(50) not null unique,Check_out_date date not null,bill_amt bigint(10) not null);")
        k=input("Enter checkout date yyyy-mm-dd : ")
        co_room=int(input("Enter your room no. : "))
        floor_no=(co_room)//10
        
        query="select * from floor"+str(floor_no)+" where room_no="+str(co_room)+ " ;"
        executer(query)
        z=allfetcher()[0]
        b,c,d,e,g=z[1],z[2],z[3],z[4],z[-1]

        room_type1=(((co_room)%10)//2)+1
        ratelist={1:1500, 2:2000, 3:800, 4:1100, 5:5000 }
        l=ratelist[room_type1]*g
        
        m="insert into past_visitors(cust_name ,cust_address , ph_no,c_email ,Check_out_date,bill_amt) values ('{}','{}',{},'{}','{}',{})".format(b,c,d,e,k,l)
        executer(m)
        conn.commit()
        x="delete from floor"+str(floor_no)+" where room_no="+str(co_room)+ " ;"
        executer(x)
        conn.commit()

        time.sleep(0.5)
        print("\n\nCheckout Successful")
        time.sleep(1)
        input("Press Enter to Continue.......")

    def checkin():
        time.sleep(1)
        print('~'*90)
        print("\t\t\tRATE LIST")
        print("1) Dulex Room : 1500/-\t\t \t2) Dulex Room (AC) : 2000/- \n\n3) Regular Room : 800/-\t\t \t4) Regular Room (AC) : 1100/-\n\n5) Luxary 5 Star Room (AC) : 5000/-")
        while True:
            print()
            i_ques3=int(input("Enter the type of room you are looking for : "))
            i_ques4='floor'+input("Enter the floor you want a room at. : ")
            executer('select * from '+i_ques4+';')
            val=allfetcher()
            global c
            c=0
            for i in val:
                if i[-3]==i_ques3:
                    c+=1
            if c<2:
                cust_details(i_ques4,i_ques3)
                time.sleep(1)
                print()
                input('Press Enter to continue.........')   ####
                break
            else :
                print("\nSORRY! Room type not available at that floor. Look at another floor\n")
                time.sleep(1)
                pass


    def key_change():
        new_key=input("Enter new Master Key : ")
        executer("update pass set passw='{}' where userid='{}' ".format(new_key,'Master_key'))
        conn.commit()
        time.sleep(1.25)

    def passcreater(key12): 
        if key12=="147258369":
            s="create table if not exists pass(login_type varchar(20) not null , userid varchar(20) not null unique primary key , passw varchar(25) not null);"   ###
            executer(s)    
            try:
                t=i_1
                u='Master_key'
                p='147258369'
                executer("insert into pass(login_type , userid , passw) values('{}','{}','{}')".format(t,u,p))
                conn.commit()
                t='Manager'
                u='Manag1010'
                p='1010m'
                executer("insert into pass(login_type , userid , passw) values('{}','{}','{}')".format(t,u,p))
                conn.commit()
                t='Receptionist'
                u='Recep1010'
                p='1010r'
                executer("insert into pass(login_type , userid , passw) values('{}','{}','{}')".format(t,u,p))
                conn.commit()
                print("~"*90)
                print("Initial Credentials created, if you wish to cahange the credentials choose update credentials in the login screen")
                print("Redirecting to login screen.........")
                time.sleep(1)
            except :
                print("Credentials already created. You may proceed to login to your system or update credentials.")
                print("Redirecting to login screen.........")
                time.sleep(1)
            login()
        else:
            print("\t\t\tMaster key invalid")
            print("Redirecting to login screen........")
            time.sleep(1)
            login()
            
    def passupdater(key):
        global xyz
        print("\n"+"~"*90)
        executer("select passw from pass where userid='Master_key';")
        if key==allfetcher()[0][-1]:
            print("\nFor which login_type you want to update credentials? :")
            print("1. Manager")
            print("2. Receptionist\n")
            i=int(input("Your choice : "))
            print()
            if i==1:
                a=input("Enter old user name : ")
                b=input("Enter old Password : ")
                passcheckerm(a,b)
                if xyz == 1:
                    print("\n\nChanging Userid first\n")
                    j1=input("Enter new user name for Manager : ")
                    executer("update pass set userid = '{}' where login_type = '{}'".format(j1,'Manager'))
                    conn.commit()
                    print("Now updating password")
                    j2=input("Enter new password for Manager : ")
                    executer("update pass set passw = '{}' where login_type = '{}'".format(j2,'Manager'))
                    conn.commit()
                    xyz=0
            elif i==2:
                a=input("Enter old user name : ")
                b=input("Enter old Password : ")
                passcheckerr(a,b)
                if xyz==6:
                    print("\n\nChanging Userid first\n")
                    j1=input("Enter new user name for Receptionist : ")
                    executer("update pass set userid = '{}' where login_type = '{}'".format(j1,'Receptionist'))
                    conn.commit()
                    print("Now updating password")
                    j2=input("Enter new password for Receptionist : ")
                    executer("update pass set passw = '{}' where login_type = '{}'".format(j2,'Receptionist'))
                    conn.commit()
                    xyz=0
            else:
                print("Wrong input!\nRedirecting to login screen........")
                time.sleep(1)
            login()
        else:
            print("\t\t\tMaster key invalid")
            print("Redirecting to login screen........")
            time.sleep(1)
            login()


    def passcheckerm(a,b):
        executer("select userid from pass where login_type='Manager';")    ####
        k=allfetcher()
        executer("select passw from pass where login_type='Manager' ;")    ####
        r=allfetcher()
        if a==k[0][0] and b==r[0][0]:
            global xyz
            xyz=1
        else:
            print("\nPassword and User ID combination are inappropriate")
            print("Redirecting to Login Screen\n")
            time.sleep(1)
            login()

    def passcheckermcall(a,b):
        executer("select userid from pass where login_type='Manager';")    ####
        k=allfetcher()
        executer("select passw from pass where login_type='Manager' ;")    ####
        r=allfetcher()
        if a==k[0][0] and b==r[0][0]:
            manager()
        else:
            print("\nPassword and User ID combination are inappropriate")
            print("Redirecting to Login Screen\n")
            time.sleep(1)
            login()
            
    def passcheckerr(a,b):
        executer("select userid from pass where login_type='Receptionist';")
        k=allfetcher()
        executer("select passw from pass where login_type='Receptionist';")
        r=allfetcher()
        print(k[0][0])
        if a==k[0][0] and b==r[0][0]:
            global xyz
            xyz=6
        else:
            print("\nPassword and User ID combination are inappropriate")
            print("Redirecting to Login Screen\n")
            time.sleep(1)
            login()

    def passcheckerrcall(a,b):
        executer("select userid from pass where login_type='Receptionist';")
        k=allfetcher()
        executer("select passw from pass where login_type='Receptionist';")
        r=allfetcher()
        if a==k[0][0] and b==r[0][0]:
            receptionist()
        else:
            print("\nPassword and User ID combination are inappropriate")
            print("Redirecting to Login Screen\n")
            time.sleep(1)
            login()       

    def login():
        print('~'*90)
        print("\t\t\tWelcome to Login Screen")
        print('~'*90)
        print("\t\tChoose any from the folloing options using their number assigned")
        print("\t\t\t1. Manager")
        print("\t\t\t2. Receptionist")
        print("\t\t\t3. Create logins")
        print("\t\t\t4. Update logins")
        print("\t\t\t5. Exit System")
        log=int(input("Enter your choice : "))
        if log==1:
            a=input("Enter user name : ")
            b=input("Enter Password : ")
            passcheckermcall(a,b)
        elif log==2:
            a=input("Enter user name : ")
            b=input("Enter Password : ")
            passcheckerrcall(a,b)
        elif log==3:
            j=input("Enter Master key for this system : ")
            passcreater(j)
        elif log==4:
            j=input("Enter Master key for this system : ")
            passupdater(j)        
        elif log==5:
            print()
            print('~'*90)
            print("\t\t\tThanks for service")
            print("You can restart system anytime by same interface, just type initiation() on command line")  #### initiation() use karne wali line add kar apne according, iss statement ke bracket ke andar hi.
        else:
            print("Select Valid option")
            login()
            
    def manager():
        print('~'*90)
        print('\t\t\tMAIN MENU')
        print()
        print("Welcome Manager")
        print()
        print("\t1) CheckIn.\t\t2) Customer Details\n\t3) CheckOut\t\t4) Register Staff Member\n\t5) Watch Staff details \t\t6) Logout \n\t7) See the Master key")
        print()
        ch1 = int(input("Select your choice  :  "))
        try:
            if(ch1 == 1):
                checkin()
                manager()
            elif (ch1 == 2):
                cust_details_output()
                manager()
            elif(ch1 == 3):
                checkout()
                manager()
            elif (ch1==4):
                reg_staff()
                manager()
            elif ch1==5:
                staffdetailer()
                manager()
            elif(ch1 ==6):
                print()
                print()
                print('~'*90)
                print('You have been logged out')
                login()
            elif ch1==7:
                time.sleep(0.7)
                executer("select passw from pass where userid='Master_key';")
                print("\nMaster key is → "+allfetcher()[0][-1]+"\n")
                print("Do you wish to change  Master Key? \n\t1)Yes\n\t2)No, proceed further.")
                i_key=input("\nYour choice : ")
                if i_key=='2':
                    time.sleep(1)
                    pass
                elif i_key!='1' and i_key!='2':
                    print("Wrong input!\nGoing back to Main Menu........")
                    time.sleep(1)
                    pass
                else:
                    key_change()
                manager()
            else:
                print("INVALID INPUT !! TRY AGAIN !!\n")
                manager()
        except Exception as e:
            print(e)
            print("~"*90)
            print("ERROR! GOING BACK TO MAIN MENU")
            time.sleep(1)
            manager()

    def receptionist():
        print('~'*90)
        print('\t\t\tMAIN MENU')
        print()
        print("Welcome receptionist")
        print()
        print("\t1) CheckIn.\t\t2) Customer Details\n\t3) CheckOut\t\t4) Logout")
        print()
        ch1 = int(input("  select your choice  :  "))
        try:
            if(ch1 == 1):
                checkin()
                receptionist()
            elif (ch1 == 2):
                cust_details_output()
                receptionist()
            elif(ch1 == 3):
                checkout()
                receptionist()
            elif(ch1 ==4):
                print()
                print()
                print('~'*90)
                print('You have been logged out')
                login()
            else:
                print("INVALID INPUT !! TRY AGAIN !!\n")
                receptionist()
        except Exception as e:
            print(e)
            print("~"*90)
            print("ERROR! GOING BACK TO MAIN MENU")
            time.sleep(1)
            receptionist()

    def initiation():
        key=147258369
        print('~'*90)
        print("\t\t\tWelcome to Hotel Management System")
        print('~'*90)
        start=input("Would you like to begin the system (y/n): ")
        print('~'*90)
        if start[0].lower()=='y':
            print("Initiating System")
            time.sleep(1)
        else:
            print('~'*90)
            print("You can restart system anytime by same interface, just type initiation() on command line")
            print('~'*90)
            print("thanks for service")
            return("")
        global i_1
        i_1=input("Enter Hotel's name : ")                      # Hotel name take any!!!
        i_2='create database if not exists '+i_1+';'        
        executer(i_2)
        executer('use '+i_1+';')
        global i_ques2
        i_ques2=int(input("Enter number of floors in your hotel :"))
        i_3="create table if not exists floor"
        i_4=" (room_no int(3) not null primary key, cust_name varchar(20) not null,cust_address longtext not null, ph_no bigint(20) not null unique, c_email varchar(100) unique, room_type int(1) not null,Check_in_date date not null, Day_duration int(5) not null);"
        for i in range (1,i_ques2+1):
            k=str(i)
            s=i_3+k+i_4
            executer(s)
        i_5="create table if not exists staff"
        i_6=" (st_id varchar(3) not null primary key, st_name varchar(20) not null,st_address longtext not null, st_phno bigint(20) not null unique, st_emailid varchar(100) not null unique, st_job varchar(20) not null,st_salary int(9) not null,st_floor int(4) not null);"
        s=i_5+i_6
        executer(s)
        login()
    initiation()