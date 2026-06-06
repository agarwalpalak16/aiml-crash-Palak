try:
 number=int(input('enter a numer'))
 if number%2==0:
     print("even")
 elif number==0:
     print("zero")
 else:
     print("odd")    

except:
   print("invalid syntax")        