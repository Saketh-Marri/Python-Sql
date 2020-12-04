import main_menu
import student_data
import mysql.connector as co
def STU_MENU():
    while True:
        #student_data.clrScreen()
        print("\t\t...................................................")
        print("\t\t................welcome to school management system")
        print("\t\t...................................................")
        print("\n\t\t........Student Data Menu........")
        print("1: Add Student Record")
        print("2: Show Student Details")
        print("3: Search Student Records")
        print("4: Delete Student Records")
        print("5: Edit Student record")
        print("6: Exit")
        print("\t\t---------------------------------------------------")
        choice=int(input("enter your choice 1-6"))
        if choice==1:
            student_data.Add_Records()
        elif choice==2:
            student_data.Show_Stu_Details()
        elif choice==3:
            student_data.Search_Stu_Details()
        elif choice==4:
            student_data.Delete_Stu_Details()
        elif choice==5:
            student_data.Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice try again....")
            conti = input("Press any key to continue")

def Add_Records():
    try:
        mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
        cursor=mycon.cursor
        session=input('Enter academic session(2019-20')
        stname=input("enter Student Name:")
        stclass=input("Enter Class:")
        stsec=input('Enter Section')
        stroll=input("Enter roll no")
        sub1 = input("Enter subject 1:")
        sub2 = input("Enter subject 2:")
        sub3 = input("Enter subject 3:")

        query="insert into student(session,stname,stclass,stsec,stroll,sub1,sub2,sub3"
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in the Student Table")
    except:
        print("error")

def Show_Stu_Details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for row in data:
        print(row)

def Search_Stu_Details():
    mycon=co.connect(host="localhost",user="root",passwd="",database="MPS")
    cursor=mycon.cursor
    ac=input("enter roll number")
    st="select * from student where stroll='%s'"%(ac)
    cursor.execute(st)
    data=cursor.fetchall()
    print(data)

def Delete_Stu_Details():
    mycon = co.connect(host="localhost", user="root", passwd="", database="MPS")
    cursor = mycon.cursor
    ac=input("enter roll no")
    st="delete from student where stroll='%s'"%(ac)
    cursor.execute(st)
    mycon.commit()
    print('Data deleted successfully')


