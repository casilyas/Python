

def toplama():
    lst=[]
    while True:
        arg=int(input())
        if arg==0:
            break
        lst.append(arg)
    topla=0
    for i in lst:
        topla +=i
    return topla    
    

    
def cixma():
    lst=[]
    while True:
        arg=int(input())
        if arg==0:
            break
        lst.append(arg)
    cixma=0
    for i in lst:
        cixma -=i
    return cixma  

    
def vurma():
    lst=[]
    while True:
        arg=int(input())
        if arg==0:
            break
        lst.append(arg)
    vurma=1
    for i in lst:
        vurma *=i
    return vurma   
    
    
def bolme():
    lst=[]
    while True:
        arg=int(input())
        if arg==0:
            break
        lst.append(arg)
    bolme=1
    for i in lst:
        bolme /=i
    return bolme  
    
def calc():
    
   while True:
     n=str(input(print("istediyiniz funksiyani qeyd edin \n+ \n - \n *\n /\n")))
     if n=="+":
        print(toplama())
     elif n=="-":
          print(cixma())
     elif n=="*":
        print(vurma())
     elif n=="/":
        print(bolme())  
     elif n=="exit":
         break                                      
     else:
        print("invalid value")     
     
        
     
        
calc()











