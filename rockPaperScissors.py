import random 
import os
import re
os.system('cls' if os.name=='nt'else'clear')
while(1<2):
    print ("\n")
    print ("rock , paper , scissors- shoot!")
    userChoice = input("choose your weapon [R]ock ,[S]cissors or [P]aper.\n")
    if not re.match("[SsRrPp]",userChoice):
        print("please choose a letter : ")
        print("[R}ock, [S]cissors or [P]aper.")
        continue
   # //Echo the userChoice
    print ("you choose : " + userChoice)