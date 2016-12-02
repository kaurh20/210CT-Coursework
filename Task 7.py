while True: #loop
    number = input("enter number:")
    is_prime =  True
    for factor in range (2,int(number**0.5)):
        if number % factor == 0:
            is_prime =  False
    if is_prime == True:
        print ("%d prime")  
    else:
        print  ("%d not prime") %number 
        
        
