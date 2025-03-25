import os

def load_clients(filename="clients.txt"):
    clients = {}
    
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    afm, fullname, email, phone_num = parts
                    clients[afm] = {"fullname": fullname, "email": email, "phone_num": int(phone_num)}
    return clients

def save_clients(clients, filename="clients.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for afm, data in clients.items():
            file.write(f"{afm},{data['fullname']},{data['email']}, {data['phone_num']}")
                

def add_client(clients):
    afm = input("enter clients' afm: ")

    if afm in clients:
        print("The client already exists.")
    
    fullname = input("enter clients' full name: ")
    email = input("enter clientss' eimail: ")
    phone_num = int(input("enter client's phone number: "))
    
    clients[afm] = {"fullname": fullname, "email": email, "phone_num": phone_num}
    save_clients(clients)
    
    
    
def search_client(filename ="clients.txt"):
    search_c = input("enter clients' afm or part of his name to search: ")

    found = False
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8")as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    afm, fullname, email, phone_num = parts
                    if search_c in afm.lower() or search_c in fullname.lower():
                        print(f"Clients' AFM: {afm}\nFullName: {fullname}\nEmail: {email}\nPhone Number: {phone_num}")
                        found = True
    if not found:
        print("client not found.")
        

def display_clients(filename = "clients.txt"):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    afm, fullname, email, phone_num = parts
                    print(f"AFM: {afm}\nFullName: {fullname}\nEmail: {email}\nPhone Number: {phone_num}")

def main():
    clients = load_clients()

    while True:
        print("\n1. Εισαγωγή νέου πελάτη")
        print("2. Αναζήτηση πελάτη")
        print("3. Εμφάνιση όλων των πελατών")
        print("0. Έξοδος")
        choice = input("Επιλέξτε ενέργεια (0-3): ")

        if choice == "1":
            add_client(clients)
            save_clients(clients)
        elif choice == "2":
            search_client()
        elif choice == "3":
            display_clients()
        elif choice == "0":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Δοκιμάστε ξανά.")

if __name__ =="__main__":
    main()