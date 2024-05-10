# Class1
# hi = 1701
# print(hi)

#-----------------------------=====================================------------------------------#
#>--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<-#

# 𝘤𝘭𝘢𝘴𝘴𝟮
age=1
if age>= 18:
    print("You are eliigible to vote")
else:
    print("your are child")


# Grade
per = 44
if per>=85:
    print("Destination")
elif per>=75:
    print("First Class")
elif per>=60:
    print("Second Class")
elif per >=50 or 40:
    print("Third Class")
elif per >=35:
    print("Pass")
else:
    print("Fail")


# sum,sub,mul
a=2
b=2
sum = a + b 
sub=a-b
mul=a*b
div=a/b
mod=a%b
print("2 + 2 =",sum)
print("2 - 2 =",sub)
print("2 * 2 =",mul)
print("2 / 2 =",div)
print("2 % 2 =",mod)



# Class3

def add(aa):
    if aa<=5:
        print(aa)
        add(aa + 1)
add(1)




def add():
    global x
    x = 10

add()
print(x)




y="string"
print(y)



 #-----------------------------===============New Class================------------------------------# 
#>--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<-#
zz=[1,2,3,4,5,6]
print(zz)
print(zz[0])

for zy in zz:
    print(zy)

(a.append(20))    #it will add new number 
print(zz)


a.insert(0,10)    #it will add in a first 
print(zz)


zz[0] = 100
print(zz)


print(zz.index(100))   #it will find number place  it will show :---- 0



zz.pop(1)  #it will remove 1
print(zz)


zz.remove(6) #it will remove value bases 6th place
print(zz)


zz.reverse()# it will reverse the number 
print(zz)

print(zz.count(5))   #find repetation of number

zz2 = [7,8]
zz.extend(zz2)
print(zz)


import array 
az = array.array('i' ,[1,2,3,4,5])  #i-int f-float u-charcter
print(a[0])

 #-----------------------------=====================================------------------------------# 
#>--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<->-<->--<-#
#swaping program
a1=10
b1=30
print("a=",a1, "b=",b1)
c1=a1
a1=b1
b1=c1
print("a=",a1, "b=",b1)


a1=a1+b1  # *
b1=a1-b1    # -
a1=a1-b1  # -
print(a1,b1)


#
a2 = 'e'
if a2>='a' and a2<='z':
    print('lower')
elif a2>='A' and a2<='Z':
    print("Upper")

elif a2>='0' and a2<='9':
    print("Number")

else:
    print("special char")


a3=1
b3=30
c3=40
if a3==1:
    print(c3+b3)
elif a3==2:
    print(b3-c3)
elif a3==3:
    print(b3*c3)
elif a3==4:
    print(b3/c3)
else:
    print("Invalid")





a4=4
# if a4%2==0:
# print("Even")

if a4>=1:
    print("pos")
elif a<=-1:
    print("neg")

else:
    print("zero")



a5=2   #table
for b5 in range(1,11,1):
    print(a5,"*", b5, "=", a5*b5)


#sum of series
import math
a6=5
print(math.factorial(a5))
for b6 in range (1,6,1):
    sum=sum+b6
    print(sum)



    sum1=0
    for c6 in range (2,11,2):
        sum1=sum+c6
        print(sum1)

a7=65
print(chr(a7))   #output ---> A


a8="mom"
if(a8==a8[::-1]):
    print("yes")
else:
    print("no")


    n1 = 0
    n2 = 1
    n0=1
    print(n1)
    print(n2)
    while(n0<=5):
        n3=n1+n2
        print(n3)
        n1=n2
        n2=n3
        n0=n0+1



        b0=[1,2,3,4,5]
        c0=100
        sum=0
        for I in range(0, 4, 1):
            sum = sum + b[I]
            print(sum)
#   for j in range(0,4,1):
    if b0[I]==c0:
        print("present")
    else:
        print("not")

    
    

r=65
for A in range (1,4,1):
    for B in range (0,A,1):
        print(chr(r),end=" ")
        r= r+1
        print("\n")






















