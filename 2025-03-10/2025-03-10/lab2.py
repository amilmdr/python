import cmath
fnum = int(input("Enter your f num: "))  
snum = int(input("Enter your f num: "))
z = complex(fnum,snum)

if(fnum==snum):
    print('hello')
elif(fnum<snum):
    print('fnam is less than snum')
else:
    print('in am in  else')

print('hello') if  fnum > snum else print('=') if fnum==snum else print('hello world')


if(fnum>snum):
    print('hello')
else:
 
    if(fnum==snum):
      print('=')
    else:
        print('hello world')


a= 33
b=200
if b >  a :
    pass