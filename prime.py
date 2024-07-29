x= int(input("any no"))
if x>1:
    is_prime= True
    for i in range(2,x):
        if x% i == 0:
            is_prime = False
            break
    if is_prime:
        print (x,"is prime")
    else: 
        print(x,"is not prime") 

 