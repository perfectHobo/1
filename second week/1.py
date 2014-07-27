
# Напишите функцию input_int(a, b), которая будет работать.
# так же как функция input() без параметров, но только она
# будет проверять, что введённая пользователем строка
# действительно является числом в интервале [a;b],
# и если это не так, то будет просить пользователя повторить попытку ввода
def input_int(minnum, maxnum):
    userinp = input()
    while True:
        if userinp.isdigit() and minnum < int(userinp) < maxnum:
            input()
            break
        else:
            print ("повторите попытку")
            break
    return userinp
minnum = 1
maxnum = 20
input_int(minnum, maxnum)



 


    
        
    
        
    
    
            



   
    
     



