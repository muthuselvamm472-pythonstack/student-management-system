from nt import error
from os import name
import db

def validate_student(name, email, mark):
    if not name:
        return "Name cannot be empty"
    at = email.find("@")
    if at < 1 or "." not in email[at + 1:]:
        return "Enter a valid email"
    if not 0 <= mark <= 100:
        return "Enter the mark between 0 and 100"
    return None



def add_option():
    try:
        NAME=input("ENTER YOUR NAME: ")
        EMAIL=input("ENTER YOUR EMAIL: ")
        COURSE=input("ENTER YOUR COURSE: ")
        MARK=float(input('ENTER YOUR MARK: '))           
    except ValueError:
        print('Mark must be a number')
    else:
        name=NAME.strip()
        Email=EMAIL.strip()
        course=COURSE.strip()
        error=validate_student(name,Email,MARK)
        if error:
            print(error)
            return
            
        if db.add_student(name,Email,course,MARK):
            print("Student added")
        else:
            print("Could not add student (email already exists)")
def view_option():
    rows=db.view_student()
    if not rows:
        print('table is empty')
    else:
        for row in rows:
            print(f'ID:{row[0]}||Name:{row[1]}||Email:{row[2]}||Course:{row[3]}||Mark:{row[4]}')

def search_option():
    try:
        ID=int(input("Enter the id:"))
        row=db.search_student(ID)
    except ValueError:
        print("ID should be integer!!!")
    else:
        if row is None:
            print("No student found with that ID")
        else:  
            print(f'ID:{row[0]}||Name:{row[1]}||Email:{row[2]}||Course:{row[3]}||Mark:{row[4]}')

def update_option():
    try:
        ID=int(input("ENTER THE CHANGING PERSON ID:"))
        NAME=input("ENTER YOUR NAME:")
        EMAIL=input("ENTER YOUR EMAIL:")
        COURSE=input("ENTER YOUR COURSE:")
        MARK=float(input('ENTER YOUR MARK:'))
    except ValueError:
        print('Mark or ID should be in number!!!')
    else:
        name = NAME.strip()
        email = EMAIL.strip()
        course = COURSE.strip()
        error = validate_student(name, email, MARK)
        if error:
            print(error)
            return

        res = db.update_student(name, email, course, MARK, ID)
        if res is None:
            print("Could not update student (email already exists)")
        elif res == 0:
            print("No student found with that ID")
        else:
            print("Student updated")

def delete_option():
    try:
        ID=int(input("Enter the id:"))
        res=db.delete_student(ID)
    except ValueError:  
        print("ID must be an integer")
    else:
        if res == 0:
             print("No student found with that ID")
        else:
            print("Student DELETED")



def main():
    db.create_table()
    while True:
        print("\n1. Add  2. View  3. Search  4. Update  5. Delete  6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_option()
        elif choice == "2":
            view_option()
        elif choice == "3":
            search_option()
        elif choice == "4":
            update_option()
        elif choice == "5":
            delete_option()
        elif choice=="6":
            print("goodbye!!!")
            break
        else:
            print("invalid option")
            
if __name__=="__main__":
    main()
