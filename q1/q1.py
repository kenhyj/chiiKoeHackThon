#  https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
import sqlite3 as sl
import sys

# CREATES TABLE BOOK 

def create_table_book(con):
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

def create_book_entries(con):
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
    print("todo")

def check_isbn_format(isbn: str):
    """
    do not include any spaces
    isbn is 10 digit before 2007 o.w. 13 digits
    """
    isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
    return ( 10 == len(isbn_clean) or 13 == len(isbn_clean) ) and (isbn_clean.isdecimal())


def get_book_info (con, isbn: str):
    """
    """
    if (check_isbn_format(isbn)):
        isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
        # call the DB
        with con: 
            data= con.execute("SELECT * FROM BOOK WHERE isbn = "+isbn_clean)
            for row in data:
                print(row)
    else:
        print("Please check your isbn format")
        isbn_clean = isbn.strip().replace(" ", "").replace("-", "")
        if (not isbn_clean.isdecimal()): 
            print("your isbn includes a non numeric character")
        if (10 == len(isbn_clean) or 13 == len(isbn_clean)):
            print("your isbn has to include 10 or 13 numeric characters")

    def store_N_books (): 
        print ("brb")

def main ():
    con = sl.connect('q1.db')
    create_table_book(con)
    if len(sys.argv) < 2:
        create_book_entries(con)
        print ("created some dummy entries for books")

    get_book_info(con, sys.argv[1])
    # print("testing 1 2 ")


main()


