import os


def load_books(filename="library.txt"):
    books = {}
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    isbn, title, author, year = parts
                    books[isbn] = {"title": title, "author": author, "year": int(year)}
    return books



def save_books(books, filename="library.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for isbn, data in books.items():
            file.write(f"{isbn},{data['title']},{data['author']},{data['year']}")    

    
def add_book(books):
    isbn = input("Enter book isbn: ")
    
    if isbn in books:
        print("Book already exists.")
        return
    title = input("Enter book title: ")
    author = input("Enter authors' name: ")
    year = int(input("Enter books' year: "))
    
    books[isbn] = {"title": title, "author": author, "year": year}
    save_books(books)
       


def search_book(filename="library.txt"):
    search_b = input("Enter book isbn or book title to search\n").lower()
    
    found = False
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4: 
                    isbn, title, author, year = parts
                    if search_b in isbn.lower() or search_b in title.lower():
                        print(f"Book ISBN:{isbn} ,Title: {title}, Author: {author}, Year: {year}")
                        found = True
    
    if not found:
        print("Book not found")
        
        
        
def display_books(filename="library.txt"):
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4: 
                    isbn, title, author, year = parts
                    print(f"Book ISBN:{isbn} ,Title: {title}, Author: {author}, Year: {year}")
                        

def main():
    books = load_books()

    while True:
        print("\n1. Εισαγωγή νέου βιβλίου")
        print("2. Αναζήτηση βιβλίου")
        print("3. Εμφάνιση όλων των βιβλίων")
        print("0. Έξοδος")
        choice = input("Επιλέξτε ενέργεια (0-3): ")

        if choice == "1":
            add_book(books)
            save_books(books)
        elif choice == "2":
            search_book()
        elif choice == "3":
            display_books()
        elif choice == "0":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Δοκιμάστε ξανά.")


if __name__ =="__main__":
    main()