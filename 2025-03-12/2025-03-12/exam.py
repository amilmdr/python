age = int(input("Enter your f num: "))  
nation = input("Enter your f num: ").upper()
print(nation in ('NEPLAI','NEPALIESE'))
if nation in ['NEPLAI','NEPALIESE'] :
    if  age >= 18 :
        print("You are eligible to vote")
    else :
        print("You are not eligible to vote")
else:
   print("You are not eligible to vote")

