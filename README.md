# Terminal-Library_Management

There are three actors in this program, namely, librarian, user and
books.
The books will have author, name, publication company, rented date,
rented user.
The librarian can add books. The librarian will have fields such as
name and contact information.
The user will register in the library by providing his name, contact
informat
The users may take the books for rental. The users will have name,
fees and contact details. The user will have registration and login.
Design a SQL database with tables users, librarian, books.
Design a menu to
a) add user, add librarian, add books.
b) update user details, update books details
c) delete user, delete books
d) read the books details and list of books available
e) perform rental operations
If a book rented date has been updated for two weeks, then the book
should be notified to the librarian and user.
If a book is rented out for more than 20 days, fine will be added to
the user. The fine will be cummulative after every 5 days after that.
eg: After 20 days, the fine will be Rs. 20, after 5 days, it will be
20+25, after another 5 days it will be 20+25+30.
