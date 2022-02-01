#  https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
from multiprocessing.connection import Connection
import sqlite3 as sl
import sys

# CREATES TABLE BOOK 

def create_table_book(con: Connection):
    with con: con.execute("""
    CREATE TABLE IF NOT EXISTS BOOK (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        isbn TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        author TEXT,
        language TEXT
    )
    """)

# let's include some dummy entry 
# please note that "same books" but of different languages still have different isbn. 
# eg. harry potter english vs harry potter chinese

def create_book_entries(con: Connection):
    sql = "INSERT INTO BOOK(isbn, title, author, language) values (?, ?, ?, ?)"
    data = [
        ("0000000000", "Alice in Wonderland",  "Alice", "Aboriginal Canadian"),
        ("0000000000000", "Bob the Builder", "Bob", "Braille"),
        ("1111111111", "Charlie's Angel", "Charlie", "Chinese"),
        ("1111111111111", "Darwinism", "Darwin", "Dehong"),
        ("2222222222", "Elephant in the Room" , "Eli", "English"),
        ("2222222222222", "Histoire de Francis Drake", "Frank", "French"),
    ]
    with con:
        con.executemany(sql, data)

def check_isbn_format(isbn: str):
    """ (str) -> boolean
    do not include any spaces
    isbn is 10 digit before 2007 o.w. 13 digits
    """
    isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
    return ( 10 == len(isbn_clean) or 13 == len(isbn_clean) ) and (isbn_clean.isdecimal())


def get_book_info (con: Connection, isbn: str):
    """
    """
    if (check_isbn_format(isbn)):
        isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
        
        # call the DB
        with con: 
            data= con.execute("SELECT * FROM BOOK WHERE isbn = ?", [isbn_clean])
            for row in data:
                book = row
                print(row)
        return book
    else:
        print("Please check your isbn format")
        isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
        if (not isbn_clean.isdecimal()): 
            print("your isbn includes a non numeric character. \n Please not that dashes and spaces will be automatically omitted.")
        if (10 == len(isbn_clean) or 13 == len(isbn_clean)):
            print("your isbn has to include 10 or 13 numeric characters")

memoryBook = {}

# decorator
def store_books ( func ): 
    """
    Write a wrapper function that increase performance by keeping results
    in memory for the quick look up. To prevent memory from growing unbounded,
    we only want to store a maximum of N book records. At any given time, 
    we should be storing the N books that accessed most recently. 
    Assume that N can be a large number when choosing data structure(s) and
    algorithm(s)
    """
    # wrapper
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        if len(memoryBook) > 100: # N = 100 here
            # https://stackoverflow.com/questions/1756992/how-to-remove-the-oldest-element-from-a-dictionary
            memoryBook.pop(next(iter(memoryBook)))
    return wrapper

@store_books    
def store( book ):
    memoryBook.update( {book[1]: book } )

def main ():
    con = sl.connect('q1.db')
    create_table_book(con)
    if len(sys.argv) < 2:
        create_book_entries(con)
        print ("created some dummy entries for books")
    else:
        book=get_book_info(con, sys.argv[1])

    store(book) # 
    for x in memoryBook:
        print (x)


main()


