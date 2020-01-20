import sqlite3 as lite


#functionality

class DatabaseManage(object):

    def __init__(self):
        global con 
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,description TEXT,price INT,is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to create DB !")


    def insert_data(self,data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name,description,price,is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            return False

    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall() 
        except Exception:
            return False
    def delete_data(self,id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql,[id])
                return True
        except Exception:
            return False


#provide interface

def main():
    print("*"*40)
    print("\n:: Course Management :: \n")
    print("*"*40)
    print("\n")
    # object creates
    db = DatabaseManage()
    print("#"*40)
    print("\n :: User Manual :: \n")
    print("*"*40)

    print('\n1, Insert a new course\n')
    print('\n2, Show all course\n')
    print('\n3, Delete all course (need id of course)\n')

    choice = input("\n Enter a choice: ")

    if choice == "1":
        name = input("\n Enter course name: ")
        description = input("\n Enter course description: ")

        price = input("\n Enter course price: ")

        private = input("\n Is it private? ")

        if db.insert_data([name,description,price,private]):
            print("Course was inserted success")
        else:
            print("OOPs wrong")

    elif choice == "2":
        print("\n ::course List :: \n")

        for index,item in enumerate(db.fetch_data()):
            print("\n Sl no: "+str(index +1))
            print("Course ID: "+str(item[0]))
            print("Course Name: "+str(item[1]))
            print("Course Description: "+str(item[2]))
            print("Course Price: "+str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Is Private : "+private)
            print("\n")

    elif choice =="3":
        record_id = input("Enter the course ID")

        if db.delete_data(record_id):
            print("Course was Deleted  with a Success")
        else:
            print("OOPs")
            
    else:
        print("\nBAD CHOICE")


if __name__ =='__main__':
    main()





