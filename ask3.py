import os

def load_inventory(filename="inventory.txt"):
    inventory = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    code, name, price, quantity = parts
                    inventory[code] = {"name": name, "price": float(price), "quantity": int(quantity)}
    return inventory

def save_inventory(inventory, filename="inventory.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for code, data in inventory.items():
            file.write(f"{code},{data['name']},{data['price']},{data['quantity']}\n")

def add_product(inventory):
    code = input("Εισάγετε κωδικό προϊόντος: ")
    if code in inventory:
        print("Το προϊόν υπάρχει ήδη.")
        return
    name = input("Εισάγετε όνομα προϊόντος: ")
    price = float(input("Εισάγετε τιμή προϊόντος: "))
    quantity = int(input("Εισάγετε ποσότητα: "))
    inventory[code] = {"name": name, "price": price, "quantity": quantity}
    print(f"Το προϊόν {name} προστέθηκε επιτυχώς.")
    save_inventory(inventory)

def search_product(inventory):
    search_term = input("Εισάγετε κωδικό ή μέρος του ονόματος προϊόντος: ").lower()
    found = False
    for code, data in inventory.items():
        if search_term in code.lower() or search_term in data['name'].lower():
            print(f"Κωδικός: {code}\nΌνομα: {data['name']}\nΤιμή: {data['price']}\nΠοσότητα: {data['quantity']}")
            found = True
    if not found:
        print("Δεν βρέθηκε προϊόν.")

def display_inventory(inventory):
    print("\nΚωδικός | Όνομα | Τιμή | Ποσότητα")
    print("-" * 40)
    for code, data in inventory.items():
        print(f"{code} | {data['name']} | {data['price']} | {data['quantity']}")

def main():
    inventory = load_inventory()
    while True:
        print("\n1. Προσθήκη νέου προϊόντος")
        print("2. Αναζήτηση προϊόντος")
        print("3. Εμφάνιση όλων των προϊόντων")
        print("0. Έξοδος")
        choice = input("Επιλέξτε ενέργεια (0-3): ")
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            search_product(inventory)
        elif choice == "3":
            display_inventory(inventory)
        elif choice == "0":
            print("Έξοδος από το πρόγραμμα.")
            break
        else:
            print("Μη έγκυρη επιλογή. Δοκιμάστε ξανά.")

if __name__ == "__main__":
    main()