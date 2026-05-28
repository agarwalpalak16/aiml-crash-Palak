def add( a,  b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "invalid"
    else:
       return ( a/b)
    
a=int(input("enter first number"))  
b=int(input("enter second  number"))   
operation=input("enter a operation add/sub/multiply/divide")
if operation=="add":
    print(add(a , b))
elif operation=="sub":
    print(sub(a , b))    
elif operation=="multiply":
    print(multiply(a, b))
elif operation=="divide":
    print(divide(a,b))
else:
    print("invalid")    



