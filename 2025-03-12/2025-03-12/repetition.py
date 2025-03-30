#pre test loop
snum=100
enum=500
emptylist=[]
while (snum<enum):
    if(snum%7==0):
        emptylist.append(snum)
    snum+=1

print(emptylist)



snum=1000
enum=50
emptylist=[]
while (snum>=enum):
    if(snum%9==0 and snum%13==0):
        emptylist.append(snum)
    snum-=1

print(emptylist)