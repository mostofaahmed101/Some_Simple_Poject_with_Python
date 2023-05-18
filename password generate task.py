import random

letter = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

special_car = ["%","&","*","!","#","@"]

number = ["0","1","2","3","4","5","6","7","8","9"]

num_N = int(input("how many number you want in your password?? : "))
special_car_N = int(input("how many special carecture you want in your password?? : "))
letter_N = int(input("how many letter you want in your password?? : "))

passs = []

for P in range(0,num_N):
    passs += random.choice(number)

for P in range(0,special_car_N):
    passs += random.choice(special_car)

for P in range(0,letter_N):
    passs += random.choice(letter)

random.shuffle(passs)

password = ""

for p in passs:
    password += p


print(f"your generate password is {password}")


