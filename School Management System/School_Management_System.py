import student_data
import fee_details
import report
while True:
    #main_menu.clrscreen()
    print("\t\t.....................................................")
    print("\t\t...........Welcome to School Management System.......")
    print("\t\t.....................................................")
    print("\n\t\t...............Maria's Public School..........")
    print("1: Admission")
    print("2: Student Data")
    print("3: Fees Details")
    print("4: Graphic Details")
    print("5: Exit")
    print("\t\t-----------------------------------------------------")
    choice = int(input("enter your choice"))
    if choice == 1:
        admission.ADM_MENU()
    elif choice == 2:
        student_data.STU_MENU()
    elif choice == 3:
        fee_details.FEE_MENU()
    elif choice == 4:
        report.gr_rep()
    elif choice == 5:
        break
    else:
        print("Error: Invalid Choice try again....")
        conti=input("Press any key to continue")