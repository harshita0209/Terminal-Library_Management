#### 16-05-2021 Developed by HN####
import sqlite3
from typing import List
def Database():
        global conn, cursor
        #creating library database
        conn = sqlite3.connect("library.db")
        cursor = conn.cursor()
        #creating librarian,user,book tables
        cursor.execute("CREATE TABLE IF NOT EXISTS librarian (Name varchar,Contact_no integer,Password varchar)")
        cursor.execute("CREATE TABLE IF NOT EXISTS user (Name varchar,Contact_no integer,Password varchar,Book varchar,Fine integer)")
        cursor.execute("CREATE TABLE IF NOT EXISTS books (Author varchar,Name varchar,Publication varchar, rented_date date, rented_user varchar)")
def insert_user(Name,Contact_no,Pass):
    # print(Name,Contact_no)
    cursor.execute("INSERT INTO user VALUES (?, ?,?,?, ?)",(Name,Contact_no,Pass,None,0))
    conn.commit()
def insert_librarian(Name_l,Contact_no_l,Pass_l):
    # print(Name_l,Contact_no_l)
    cursor.execute("INSERT INTO librarian VALUES (?, ?, ?)",(Name_l,Contact_no_l,Pass_l))
    conn.commit()
def validate_user_credentials(N,P,Choice):
    if Choice=="1" or Choice=="3":
        cursor.execute("select count(*) from user where Name =? and Password=?",(N,P))
        count=cursor.fetchall()
        # print("count",count)
        return count
def validate_credentials(N,P,Choice):
    if Choice=="2" or Choice=="4":
        cursor.execute("select count(*) from librarian where Name =? and Password=?",(N,P))
        count=cursor.fetchall()
        # print("count",count)
        return count
    elif Choice=="9" or Choice=="7" or Choice=="8" or  Choice=="10":
        cursor.execute("select count(*) from user where Name =?",[N])
        count1=cursor.fetchall()
        # print("count",count1,N)
        return count1
def insert_book(name,author,publication):
    cursor.execute("INSERT INTO books VALUES (?, ?, ?,?, ?)",(author,name,publication,None,None))
    conn.commit()
def all_book_details(book):
    if book==None:
        cursor.execute("select * from books ")
        rows=cursor.fetchall()
        for i in rows:
            print(i)
            # print('if')
    else:
        # print(book)
        # print('else',book)
        cursor.execute("select Author,Name,Publication,rented_date,rented_user from books where Name =?",[book])
        rows=cursor.fetchall()
        print(rows)
def update_book_detail(clm,new_val,book):
    str=f"update books set {clm}='{new_val}' where Name= ?"
    cursor.execute(str,[book])
    conn.commit()
def delete_book(book):
    cursor.execute("delete from books where Name=?",[book])
    conn.commit()
def books_available():
    cursor.execute("select * from books where rented_date is NULL")
    rows=cursor.fetchall()
    for i in rows:
        print(i)
def user_info(name):
    if name==None:
        cursor.execute("select Name,Contact_no,Book,Fine from user")
        rows=cursor.fetchall()
        for i in rows:
            print(i)
    else:
        cursor.execute("select Name,Contact_no,Book,Fine from user where Name=?",[name])
        rows=cursor.fetchall()
        for i in rows:
            print(i)
def update_user(clm,new_val,name):
    str=f"update user set {clm}='{new_val}' where Name= ?"
    cursor.execute(str,[name])
    conn.commit()
    return
def delete_user(name):
    cursor.execute("delete from user where Name=?",[name])
    conn.commit()
def validate_book(name):
    cursor.execute("select count(*) from books where Name =? and rented_date is NULL",[name])
    count1=cursor.fetchall()
    # print("count",count1,name)
    return count1
def update_user_book(name_book,fine,name_user,date1):
    
    str=f"update books set rented_user='',rented_date=NULL where rented_user=?"
    cursor.execute(str,[name_user])
    str=f"update books set rented_date=?,rented_user=? where Name=?"
    cursor.execute(str,[date1,name_user,name_book])
    str=f"update user set Book= ? ,Fine=? where Name=?"
    cursor.execute(str,[name_book,fine,name_user])
    conn.commit()

def book_assigned(Name):
    cursor.execute("Select * from books where rented_user=?",[Name])
    rows=cursor.fetchall()
    for i in rows:
        print(i)
