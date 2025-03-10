fnum = int(input("Enter your f num: "))  
snum = int(input("Enter your f num: "))
complexNum=  complex(fnum,snum)
toPrintReal= "The real part  "+str(complexNum)+"is"+str(complexNum.real)
toPrintImg= "The img part "+str(complexNum)+"is"+str(complexNum.imag)
print(fnum ,snum,complexNum, toPrintReal,toPrintImg)


