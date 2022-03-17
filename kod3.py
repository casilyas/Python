import random 
a=random.randint(1,100)

a
i=1
while i<=3:
    b=int(input(print("3 sansiniz var")))
    if b!=a:
        print("kod duz deyil yeniden daxil ediin")
    elif b==a:
        print("kod dogrudur")
    elif b==0:
        break
    
    i+=1    
        
print("dogru cavab",a)        
