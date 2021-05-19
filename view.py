#### 16-05-2021 Developed by HN####
def startup_prompt():
    menu = """
    Welcome to the Terminal Library Management!
    Please enter an option:
    1. Register user
    2. Register librarian
    3. Existing user-Login
    4. Existing librarian-Login
    5. Exit
    """
    print(menu)
    choice = input()
    return choice
def incorrect_choice():
    print("Invalid option Selected.")
    return
def add_user():
    Name= input("Please enter your name: ")
    Contact_no = input("Please enter your 10 digits contact no: ")
    Pass=input("Enter password: ")
    return Name, Contact_no,Pass
def add_librarian():
    Name_l= input("Please enter your name: ")
    Contact_no_l = input("Please enter your 10 digits contact no: ")
    Pass_l=input("Enter password: ")
    return Name_l, Contact_no_l,Pass_l
def Login_success(Name):

    print(f'Congrats {Name} ! You have been successfully registered!!')
def cred_input():    
    print("Enter your credentials for login-")
    Name=input("Enter Name-")
    Password=input("Enter Password-")
    return Name,Password
def incorrect_creds():
    print("The credentials entered are incorrect.")
    return
def librarian_menue():
    menu = """
    *******Please enter your choice related to books:*******
    1. Add Book
    2. Update Book Details
    3. Delete Books
    4. Books Available
    5. All Books Details
    6. Logout

    *******Please enter your choice related to user:********
    7. Update User Details
    8. Delete User
    9. Rent a book to user
    10. User detail/All user details
    """
    print(menu)
    choice = input()
    return choice
def add_book():
    input('*******Enter Book Details*******')
    author=input('Enter Author ')
    name=input('Enter Name of Book ')
    publication=input('Enter Book publication ')
    return name,author,publication
def update_book():
    
    book=input('Enter Name of book you want to update/delete/rent or 0 to exit ')
    # if book =='0':
    #     return book
    
    return book
def update_book_coulmn():
    columns="""
    1.Author
    2.Name
    3.Publication
    4.Rented Date
    5.Rented User
    """
    print(columns)
    new_val=""
    clm=input('Enter the no. for the column you want to update or 0 for exit')
    if clm >'5':
        print(f'You have entered a wrong choice')
        return clm,new_val
    elif clm =='0':
        return clm,new_val
    else:
        new_val=input('Enter the new column value')
        # print(clm,new_val)
        return clm,new_val
def user_name():
    name=input("Enter name of user or 0 to exit-")
    return name
def user_details():
    
    col="""
    1-Name
    2-Contact no.
    """
    new_val=""
    print(col)
    clm=input('Enter the no. for the column you want to update or 0 for exit')
    if clm>'2':
        print(f'You have entered a wrong choice')
        return clm,new_val
    elif clm =='0':
        return clm,new_val
    else:
        new_val=input('Enter the new column value')
        # print(clm,new_val)
        return clm,new_val

def rent_date():
    date1=input('Enter the date in "YYYY-MM-DD" format')
    return date1
def user_menue():
    menue="""
    1. Available Books
    2. Check user details
    3. Detail of book assigned
    4. logout
    """
    print(menue)
    choice = input()
    return choice
    



