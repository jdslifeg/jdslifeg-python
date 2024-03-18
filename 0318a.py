#기본
cond=True
if cond:
    print("참")
    
#b if else
a=10
if 1<a:
    print("big")
else:
    print("small")
    
# if elif elif else
aa=input("enter in? ==> ")
aa=int(aa)
if 10<aa:
    print("big <10")
elif 5<aa:
    print("big 5<aa")
elif 3<aa:
    print("big 3<aa")
else:
    print("small 3>aa")
    
#in,not
a=[1,2,3]
print(1 in a)

aa="hello"
print("e"not in aa)


bb=input("---> ")
bb=int(bb)
cc="jang" if 100<bb else "not"
print(cc)

a=0
while a<10:
    a=a+1
    if a%3==0:
        continue
    if a%5==0:
        break
    print(a)

while true:
    a=input("While==> ")
    int(a)
    if a==0:
        print("0 ok")
        break





    
    

