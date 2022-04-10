import os
with open("oku.txt","a") as dosya:
    a=input("Enter the text input you want to give to the C# file")
    dosya.write(a)
    #The address of your c# exe file should be given to os.startfile
    os.startfile("C://Users//90553//source//repos//fileread//fileread//bin//Debug//netcoreapp3.1//fileread.exe")
