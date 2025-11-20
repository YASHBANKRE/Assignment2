logged_user = ''
id_password = {}
student_info ={}
logged = False


def register():
    print("Welcome to Registration")
    list_of_info = {}

    name = input("Enter your name: ")
    list_of_info["Name"] = name

    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    list_of_info["DOB"] = dob

    branch = input("Enter your branch: ")
    list_of_info["Branch"] = branch

    college_name = input("Enter your college name: ")
    list_of_info["College name"] = college_name

    email = input("Enter your email: ")
    list_of_info["Email"] = email

    contact_number = input("Enter your contact number: ")
    while(len(contact_number) != 10 or not contact_number.isdigit()):
        print("Invalid contact number, Please try again")
        contact_number = input("Enter your contact number: ")
    list_of_info["Contact number"] = contact_number

    home_address = input("Enter your home address: ")
    list_of_info["Home address"] = home_address

    residential_address = input("Enter your residential address: ")
    list_of_info["Residential address"] = residential_address

    cgpa = input("Enter your CGPA: ")
    list_of_info["Cgpa"] = cgpa

    father_name = input("Enter your father's name: ")
    list_of_info["Father's name"] = father_name

    father_contact = input("Enter your father's contact number: ")
    while(len(father_contact) != 10 or not father_contact.isdigit()):
        print("Invalid contact number, Please try again")
        father_contact = input("Enter your father's contact number: ")
    list_of_info["Father's contact number"] = father_contact

    mother_name = input("Enter your mother's name: ")
    list_of_info["Mother's name"] = mother_name

    mother_contact = input("Enter your mother's contact number: ")
    while(len(mother_contact) != 10 or not mother_contact.isdigit()):
        print("Invalid contact number, Please try again")
        mother_contact = input("Enter your mother's contact number: ")
    list_of_info["Mother's contact number"] = mother_contact

    id = input("Enter your enrollment number: ")
    while((id in id_password)):
        print("User already exists, try different or check your enrollment number")
        id = input("Enter your enrollment number: ")

    list_of_info["Enrollment number"] = id

    print("Be careful while setting the password: ")
    password = input()
    confirm_password = input("Confirm your password: ")
    while(password != confirm_password):
        print("Password did not match, Please try again")
        password = input("Again, enter your password: ")
        confirm_password = input("Confirm your password: ")

    id_password[id] = password
    alter_key = input("Set your security question for forgot password (What is your hometown name?): ")
    list_of_info["Security question"] = alter_key
    print("Registration Successful")
    print("Your enrollment number will be your username id ")

    print("You can now login to your account")
    student_info[id] = list_of_info
    main()


def login():
    print("Welcome to Login")
    print("Enter your id: ")
    id = input()
    if id_password.get(id) is None:
        print("User does not exist, Please register first")
        main()

    count = 1
    password = input("Enter your password: ")
    while(id_password[id] != password and count < 5):
        if(count == 4):
            print("You have entered wrong password 5 times, your account is blocked")
            main()
        count += 1
        print("Invalid password, Please try again")
        password = input("Again enter your password: ")

    print("Login Successful")
    global logged_user
    logged_user = id
    global logged
    logged = True
    print("Welcome ", logged_user)
    main()


def show_profile():
    if not logged:
        print("Please login first to view profile")
        main()
    print("Your profile details are as follows: ")
    for key, value in student_info[logged_user].items():
        if(key == "Security question"):
            continue
        print(f"{key}: {value}")
    main()


def update_profile():
    if not logged:
        print("Please login first to view profile")
        main()
    show_profile()
    print("Enter the field you want to update (Name, DOB, Cgpa, Father's name, Mother's name, Branch,College name, Email, Contact number, Home address, Residental address, Father's contact number, Mother's contact number): ")
    field = input()
    while(field not in student_info[logged_user]):
        print("Invalid field, Please try again")
        field = input("Enter the field you want to update: ")
    new_value = input(f"Enter new value for {field}: ")
    student_info[logged_user][field] = new_value
    print(f"{field} updated successfully")
    main()


def change_password():
    if not logged:
        print("Please login first to change password")
        main()
    current_password = input("Enter your current password: ")
    while(id_password[logged_user] != current_password):
        print("Incorrect password, Please try again")
        current_password = input("Enter your current password: ")
    
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    while(new_password != confirm_password):
        print("Password did not match, Please try again")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

    id_password[logged_user] = new_password
    print("Password changed successfully")
    main()


def forget_password():
    print("Welcome to Forgot Password")
    id = input("Enter your id: ")
    if id_password.get(id) is None:
        print("User does not exist, Please register first")
        main()
    alter_key = input("Enter your alternate key: ")
    while(student_info[id]["Security question"] != alter_key):
        print("Incorrect answer, Please try again")
        alter_key = input("Enter your alternate key: ")

    new_password = input("Enter new password: ")
    confirm_password = input("Confirm new password: ")
    while(new_password != confirm_password):
        print("Password did not match, Please try again")
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")
        
    id_password[id] = new_password
    print("Password changed successfully")
    main()


def logout():
    global logged_user
    global logged
    if not logged:
        print("You are not logged in")
        main()
    logged_user = ''
    logged = False
    print("Logged out successfully")
    main()

    
def terminate():
    exit()

def main():
    print("Welcome in LNCT")
    print("Student Registration Portal")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Change Password
        6. Forgot Password
        7. Logout
        8. Main Menu
        9. Exit

            select option 1/2/3/4/5/6/7/8: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        change_password()
    elif response == '6':
        forget_password()
    elif response == '7':
        logout()
    elif response == '8':
        main()
    elif response == '9':
        terminate()
    else:
        print("Invalid Choice, Please select correct option")
        main()

main()