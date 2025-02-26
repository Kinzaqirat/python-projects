# password generater 

import random
import string # to generate special character

length=int(input("Enter the length of password: "))
character=string.ascii_letters #generate alphabhats
character += string.digits #generate digits and add into character
character += string.punctuation #generate special character and add into character

password='' 
 
for i in range(length):
    password += random.choice(character) #add character to random to chose randomly character

print(f"Your password is {password}")


