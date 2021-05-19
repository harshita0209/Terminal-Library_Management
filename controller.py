#### 16-05-2021 Developed by HN####
from datetime import datetime,date
from os import error
import model,view
model.Database()
def start():
    choice=None
    # while choice !=4:
    choice=view.startup_prompt()
    if choice=='1':
        Name,Contact_no,Pass=view.add_user()
        if len(Contact_no)>10:
            print("Invalid Phone number")
            start()
        user=model.insert_user(Name,Contact_no,Pass)
        view.Login_success(Name)
        N,P=view.cred_input()
        count1=model.validate_user_credentials(N,P,choice)
        # print (count1)
        while list(count1[0])[0]==0:
            # print (count1)
            view.incorrect_creds()
            N,P=view.cred_input()
            count1=model.validate_user_credentials(N,P,choice)
        if list(count1[0])[0]>=1:
            user_trans(Name)
            
    elif choice=='2':
        Name_l,Contact_no_l,Pass_l=view.add_librarian()
        if len(Contact_no_l)>10:
            print("Invalid Phone number")
            start()
        user=model.insert_librarian(Name_l,Contact_no_l,Pass_l)
        view.Login_success(Name_l)
        N,P=view.cred_input()
        count=model.validate_credentials(N,P,choice)
        # print (count)
        while list(count[0])[0]==0:
            view.incorrect_creds()
            N,P=view.cred_input()
            count=model.validate_credentials(N,P,choice)
        if list(count[0])[0]>=1:
            lib_trans_(Name_l)
    elif choice=='3':        
        N,P=view.cred_input()
        count1=model.validate_user_credentials(N,P,choice)
        # print(count1)
        while list(count1[0])[0]==0:
            view.incorrect_creds()
            N,P=view.cred_input()
            count1=model.validate_user_credentials(N,P,choice)
        if list(count1[0])[0]>=1:
            user_trans(N)
    elif choice=='4':        
        N,P=view.cred_input()
        count1=model.validate_credentials(N,P,choice)
        # print(count1)
        while list(count1[0])[0]==0:
            view.incorrect_creds()
            N,P=view.cred_input()
            count1=model.validate_credentials(N,P,choice)
        if list(count1[0])[0]>=1:
            lib_trans_(N)
            
    elif choice=="5":
        return
    else:
        view.incorrect_choice()
        start()
# Name_l='Harry'     
def lib_trans_(Name_l):
    print(f'{Name_l} - logged in as a Librarian !')
    choice=view.librarian_menue()
    if choice=='1':
        name,author,publication=view.add_book()
        model.insert_book(name,author,publication)
        model.all_book_details(name)
        lib_trans_(Name_l)
    elif choice=='2':
        # clm,new_val=None,None
        while choice :
            book=view.update_book()
            if book=='0':
                lib_trans_(Name_l)
            print(f'{book} detail -')
            print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
            model.all_book_details(book)
            clm,new_val=view.update_book_coulmn()
        
            if clm=='1':
                clm_upd="Author"
            elif clm=='2':
                clm_upd="Name"
            elif clm=='3':
                clm_upd="Publication"
            elif clm=='4':
                clm_upd="rented_date"
            elif clm=='5':
                clm_upd="rented_user"
            elif clm=='0' or clm>'5':
                lib_trans_(Name_l)
            
            
            model.update_book_detail(clm_upd,new_val,book)
            if clm=='2':
                print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
                model.all_book_details(new_val)
            else:
                print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
                model.all_book_details(book)

    elif choice=='3':
        book=view.update_book()
        if book=='0':
                lib_trans_(Name_l)
        model.delete_book(book)
        book=None
        print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
        model.all_book_details(book)
        lib_trans_(Name_l)
    elif choice=='4':
        print("Available books/books not yet rented)")
        print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
        model.books_available()
        lib_trans_(Name_l)
    elif choice=='5':
        book=None
        print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
        model.all_book_details(book)
        lib_trans_(Name_l)
    elif choice == '6':
            start()
    elif choice == '7':
        while choice :
            name=view.user_name()
            if name=='0':
                lib_trans_(Name_l)
            count=model.validate_credentials(name,0,choice)
            # print (list(count[0])[0])
            while list(count[0])[0]==0:
                print('User does not exist')
                name=view.user_name()
                if name=='0':
                    lib_trans_(Name_l)
                count=model.validate_credentials(name,0,choice)
            if name=='0':
                lib_trans_(Name_l)
            print(f'["Name","Contact No.","Book","Fine"]')
            model.user_info(name)
            clm,new_val=view.user_details()
            
            
            if clm=='1':
                    clm_upd="Name"
            elif clm=='2':
                clm_upd="Contact_no"
            elif clm=='0' or clm>'2':
                lib_trans_(Name_l)
            model.update_user(clm_upd,new_val,name)
            if clm=='1':
                print(f'["Name","Contact No.","Book","Fine"]')
                model.user_info(new_val)
            elif clm=='2':
                print(f'["Name","Contact No.","Book","Fine"]')
                model.user_info(name)
            lib_trans_(Name_l)
    elif choice=='8':
        name=view.user_name()
        if name=='0':
                lib_trans_(Name_l)
        count=model.validate_credentials(name,0,choice)
        # print (list(count[0])[0])
        while list(count[0])[0]==0:
            print('User does not exist')
            name=view.user_name()
            if name=='0':
                lib_trans_(Name_l)
            count=model.validate_credentials(name,0,choice)
        print(f'User Info----')
        print(f'["Name","Contact No.","Book","Fine"]')
        model.user_info(name)
        if name=='0':
            lib_trans_(Name_l)
        model.delete_user(name)
        name=None
        print(f'Available users----')
        print(f'["Name","Contact No.","Book","Fine"]')
        model.user_info(name)
        lib_trans_(Name_l)
    elif choice=='9':
        name_book=view.update_book()
        if name_book=='0':
                lib_trans_(Name_l)
        count=model.validate_book(name_book)
        while list(count[0])[0]==0:
            # print(list(count[0])[0])
            print('Either book does not exist or already rented')
            name_book=view.update_book()
            if name_book=='0':
                lib_trans_(Name_l)
            count=model.validate_book(name_book)
        
        name_user=view.user_name()
        if name_user=='0':
                lib_trans_(Name_l)
        count=model.validate_credentials(name_user,0,choice)
        # print (list(count[0])[0])
        while list(count[0])[0]==0:
            print('User does not exist')
            name_user=view.user_name()
            if name_user=='0':
                lib_trans_(Name_l)
            count=model.validate_credentials(name_user,0,choice)
        date1=view.rent_date()
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        today = datetime.today()
        if date1<today:
            print('Invalid date---Enter future date')
            lib_trans_(Name_l)
        
        diff=date1-today
        fine=20
        sum=20
        days=diff.days
        if days<=20:
            sum=0
        while days>20:
            
            fine=fine+5
            sum=sum+fine
            days=days-5
            # print("days-",days,"sum",sum)
            if days<20:
                # print('true')
                sum=sum-fine
                # print(sum)
        # print(name_book,sum,name_user,date1)
        model.update_user_book(name_book,sum,name_user,date1)
        lib_trans_(Name_l)
    elif choice=='10':
        print('Enter user name or enter "All" to check all users')
        name_user=view.user_name()
        if name_user=='All':
            name_user=None
            model.user_info(name_user)
        elif name_user=='0':
            lib_trans_(Name_l)
        elif name_user!='All':
            
            count=model.validate_credentials(name_user,0,choice)
            # print (list(count[0])[0])
            while list(count[0])[0]==0:
                if name_user=='All':
                    name_user=None
                    model.user_info(name_user)
                    lib_trans_(Name_l)
                print('User does not exist')
                name_user=view.user_name()
                
                if name_user=='0':
                    lib_trans_(Name_l)
                count=model.validate_credentials(name_user,0,choice)
            # print(name_user)
            print(f'["Name","Contact No.","Book","Fine"]')
            model.user_info(name_user)
        lib_trans_(Name_l)
    else:
        view.incorrect_choice()
        lib_trans_(Name_l)
def user_trans(Name):
    print(f'{Name} - logged in as a User !')
    choice=view.user_menue()
    if choice=="1":
        print("Available books/books not yet rented)")
        print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
        model.books_available()
        user_trans(Name)
    elif choice=="2":
        print(f'["Name","Contact No.","Book Assigned","Fine"]')
        model.user_info(Name)
        user_trans(Name)
    elif choice=="3":
        print(f'[("Author","Name","Publication","Rented Date","Rented User")]')
        model.book_assigned(Name)
        user_trans(Name)
    elif choice=="4":
        start()
    else:
        view.incorrect_choice()
        model.user_info(Name)   

if __name__ == "__main__":
    # lib_trans_(Name_l)
    start()