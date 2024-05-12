import datetime

class LMS:
    """This class is used to keep a record of the library.
    It has a total of four modules: "Display books", "Issue books", "Return books", "Add books"."""
    
    def __init__(self, list_of_books, library_name): 
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.books_dict = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books_dict.update({str(Id): {"books_title": line.replace("\n", ""), "student_name": "", "Issue_date": "", "status": "Available"}})
            Id += 1

    def display_books(self):
        """Display all available books."""
        print("---------------------List of books------------------------")
        print("books Id", "\t","Title")
        print("----------------------------------------------------------")
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get("books_title"),"[",value.get("status"),"]")

    def issue_books(self):
        """Issue books to students."""
        books_id = input("Enter books ID:")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"] != "Available":
                print(f"This book is already issued to {self.books_dict[books_id]['student_name']} on {self.books_dict[books_id]['Issue_date']}")
                return self.issue_books()
            else:
                your_name = input("Enter your name:")
                self.books_dict[books_id]["student_name"] = your_name
                self.books_dict[books_id]["Issue_date"] = current_date
                self.books_dict[books_id]["status"] = "Already Issued"
                print("Books Issued successfully !!! \n")
        else:
            print("Book ID not found !!!")
            return self.issue_books()
        
    def add_books(self):
        """Add new books to the library."""
        new_books = input("Enter books title:")
        if not new_books:
            print("Book title cannot be empty!")
            return self.add_books()
        elif len(new_books) > 30:
            print("Book length is too long !!! title length should be less than 30 words")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:
                bk.write(f"{new_books}\n")
            self.books_dict[str(int(max(self.books_dict)) + 1)] = {"books_title": new_books, "student_name": "", "Issue_date": "", "status": "Available"}
            print(f"This book '{new_books}' has been added successfully !!!")

    def return_books(self):
        """Return books to the library."""
        books_id = input("Enter the books ID:")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"] == "Available":
                print("This book is already available in the library. Please check your book ID.")
            else:
                self.books_dict[books_id]["student_name"] = ""
                self.books_dict[books_id]["Issue_date"] = ""
                self.books_dict[books_id]["status"] = "Available"
                print("Successfully updated!!!\n")
        else:
            print("Book ID not found")

try:
    myLMS = LMS("list_of_books.txt", "Python's")
    press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n-----------------Welcome To {myLMS.library_name} Library management system----------\n")
        for key, value in press_key_list.items():
            key_press = input("Press key: ").lower()
            if key_press == "i":
                print("\nCurrent selection : Issue Books")
                myLMS.issue_books()
            elif key_press == "a":
                print("\nCurrent selection : Add books\n")
                myLMS.add_books()
            elif key_press == "d":
                print("\nCurrent selection : Display books\n")
                myLMS.display_books()
            elif key_press == "r":
                print("\nCurrent selection : Return books\n")
                myLMS.return_books()
            elif key_press == "q":
                break
            else:
                continue
except Exception as e:
    print("Something went wrong. Please check your input")
