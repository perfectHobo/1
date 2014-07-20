import random
pn = random.randint(1, 100) # pn - program number
print ("Разгадай какое число загадал компьютер - в промежутке от 1 до 100")
c = 0 # c - counter
while True:
    un = int(input())
    c += 1
    if pn > un:
        print ("Введи число побольше")
        continue
    elif pn < un:
        print ("Введи число поменьше")
        continue
    else: un == pn
    break
print ("Число угадано за " + str(c) + " попыток")
input()



 


    
    

 
  
