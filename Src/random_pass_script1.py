import random
import array

# charaters going to use in it

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

wordlist =[]

#length of password 
#can be change according to need
MAX_LEN = 12

password = ""


                 
         


user_decision = input("Press \"y\"  for readable password and \"n\" for random charater password:")
print (user_decision)

if user_decision == "n":
    
    LIST_of_CHAR = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    
    rand_1 = random.choice(DIGITS)
    rand_2 = random.choice(UPCASE_CHARACTERS)
    rand_3 = random.choice(LOCASE_CHARACTERS)
    rand_4 = random.choice(SYMBOLS)
    temp_pass = rand_1 + rand_2 + rand_3 + rand_4
    
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(LIST_of_CHAR)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
    

    for x in temp_pass_list:
        password = password + x
    
    
else:
    with open("..\\Password Generator\\Assets\\wordlist.txt", 'r') as file:
        data = file.readlines()
        
        for line in data:
             words = line.split()
         
             for item in words:
                 if len(item)>5 :
                     wordlist.append(item.capitalize())
    
    LIST_of_CHAR = DIGITS + wordlist + SYMBOLS
    
    rand_1 = random.choice(wordlist) 
    rand_2 = str(random.randint(10,99))
    rand_3 = random.choice(SYMBOLS)
    
    
    password = rand_1+rand_2+rand_3
    



print(password)

  





