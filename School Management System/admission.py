import main_menu
import admission
import mysql.connector as co
def ADM_MENU():
    while True:
        #admission.clrscreen()
        print("\t\t.....................................................")
        print("\t\t...........Welcome to School Management System.......")
        print("\t\t.....................................................")
        print("\n\t\t...............Maria's Public School..........")
        print("1: Admission Details")
        print("2: Show admission Details")
        print("3: Search")
        print("4: Deletion of records")
        print("5: Update Admission Details")
        print("5: Return")
        print("\t\t-----------------------------------------------------")
        choice = int(input("enter your choice"))
        if choice == 1:
            admission.admin_details()
        elif choice == 2:
            admission.show_admin_details()
        elif choice == 3:
            admission.search_admin_details()
        elif choice == 4:
            admission.delete_admin_details()
        elif choice == 5:
            admission.edit_admin_details()
        elif choice == 6:
            return
        else:
            print("Error: Invalid Choice try again....")
            conti=input("Press any key to continue")

def admin_details():
    try:
        mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
        cursor=mycon.cursor()
        adno=input("Enter Admission number")
        rno=int(input("enter roll no"))
        sname=input("enter student name")
        address=input("enter address")
        phon=input("enter phone number")
        clas=input("enter class")

        query = "insert into admission(adno,rno,sname,address,phon,clas)values('{}',{},'{}','{}','{}','{}')".format(adno,rno,sname,address,phon,clas)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in admission table")
    except:
        print("error")

def show_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()
    cursor.execute("select * from admission")
    data = cursor.fetchall
    for row in data:
        print(row)

def search_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission Number")
    st="Select * from admission where adno='%s'"%(ac)
    cursor.execute(st)
    data = cursor.fetchall()
    print(data)

def delete_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()
    ac=input('enter admission no')
    st="delete from admission where adnos='%s'"%(ac)
    cursor.execute(st)

def edit_admin_details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()


    print("1: Edit name")
    print("2: Edit Address")
    print("3: Phone Number")
    print("4: Return")
    print("\t\t---------------------------------------------")
    choice=int(input("Enter your choice"))
    if choice==1:
        admission.edit_name()
    elif choice==2:
        admission.edit_address()
    elif choice==3:
        admission.edit_phno()
    elif choice==4:
        return
    else:
        print("Error: Invalid Choice Try Again....")
        conti="Press any key to return to"

def edit_name():
    mycon=co.connect(host="localhost",user='root',passwd="",database="MPS")
    cursor=mycon.cursor()
    ac=input("enter Admission no:")
    nm=input('enter correct name')
    st="update admission set sname='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data updated successfully")

def edit_address():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()
    ac=input("enter Admission no:")
    nm=input("enter correct address")
    st="Update admission set address='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print("Data Updated Successfully")

def edit_photo():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor()
    ac=input("Enter Admission no:")
    nm=input('Enter correct phone number')
    st="Update admission set phon='%s' where adno='%s'"%(nm,ac)
    cursor.execute(st)
    mycon.commit()
    print('Data updated successfully')