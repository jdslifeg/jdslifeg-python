val=[1,2,3]
for a in val:
    print(a)
    
val=[(1,1),(2,2),(3,3)]
for(a,b) in val:
    print(a,b)

s=0
val=range(1,10)
for a in val:
    if (a%2==0):
        continue
    s=s+a
print(s)

def a():
    print("hello world")
    
a()
  

def aa(a,b=10):
    print(a)
    print(b)
    return(a*b)

print(aa(3,4))
print(aa(5))

def su(*v):
    aa=0
    for bb in v:
        aa=aa+bb
    return aa

print(su(1,2,3))

to=su(1,2,3)
print(to)

print("_____________")

def aa(a,b):
    return a+b,a-b

print(aa(4,2))
x,y=aa(4,2)
print(x)
print(y)
print(x,y)

print("_____________")
print("_____________")
ka=7
def aa(data):
    global ka
    ka=data
    data=data*10
    return data*data

data=10
bb=aa(data)
print(ka)
print("_____________")
print(data)
print(bb)

print("_____________")
print("_____________")

def aa(data):
    data[1]=33

data=[1,2,3]
aa(data)
print(data)











    

        
    