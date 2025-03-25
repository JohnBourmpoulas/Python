import random


letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = ['0','1','2','3','4','5','6','7','8','9']
password = []


length = int(input("Enter disired password length: "))
letters_length = int(input("Enter disired letters length: "))
digits_length = int(input("Enter disire digits length: "))

while letters_length+digits_length != length:
    print(f"The sum of letters and digits must be exactly {length}. Please try again.")
    letters_length = int(input("Enter disired letters length: "))
    digits_length = int(input("Enter disire digits length: "))
    
    
count_letters = 0
count_digits = 0
for i in range(length):
    if count_digits >= count_letters:
        char = random.choice(letters)
        password.append(char)
        count_letters+=1
    else: 
        number = random.choice(digits)
        password.append(number)
        count_digits+=1

random.shuffle(password)
final_password = "".join(password)
print("Generated password: ", final_password)