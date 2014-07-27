def input_int(minnum, maxnum):
    userinp = input()
    while True:
        if userinp.isdigit() and minnum < int(userinp) < maxnum:  
                print ("неошибка")
                break
        else:
            print ("ошибка")
            break
    return userinp
minnum = 1
maxnum = 20
input_int(minnum, maxnum)



 


    
        
    
        
    
    
            



   
    
     



