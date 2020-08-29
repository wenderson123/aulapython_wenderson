import time
import os
while True :

    n1 = int(input("escreva um numero : "))
  
    if (n1 % 2 )==0 :
        print(f"numero par ={n1}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print (f"impar={n1}")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

   