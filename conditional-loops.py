LOOPS:
--------------------
1
22
333
4444
55555

x=int(input(""))
for i in range(1,x+1):
  for j in range(1,i+1):
    print(i,end="")
  print()
---------------------------
Palindrome
  
num=int(input())
temp=num
rev=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
if rev==num:
  print("Palindrome")
else:
  print("Not a Palindrome")
------------------------------------
Armstrong Numbers

num=int(input())                                                                                                  
temp=num
sum=0
while num>0:
  rem=num%10
  sum=sum+rem*rem*rem
  num=num//10
if sum=temp:
  print("armstrong Number:")
else:
  print("Not an Armstrong Number")
------------------------------------------------
Calculate area of triangle, square, rectangle

fig=input("Enter figure:")
if figure=="triangle":
  b=int(input())
  h=int(input())
  print("Area:",0.5*b*h)
elif figure=="square":
  s=int(input())
  print("Area:",s*s)
else:
  l=int(input())
  b=int(input())
  print("Area:",l*b)
-------------------------------------------------------
Swapping of 3 numbers

num1=int(input())
num2=int(input())
num3=int(input())
sum=num1+num2+num3
if num1>num2 and num1>num3:
    highest=num1
elif num2>num1 and num2>num3:
    highest=num2
else:
    highest=num3
if num1<num2 and num1<num3:
    lowest=num1
elif num2<num1 and num2<num3:
    lowest=num2
else:
    lowest=num3
print(lowest,sum-(lowest+highest),highest)
--------------------------------------------------------
Fibinocci series

num=int(input())
a=0
b=1
if num!=0 and num!=1:
    print(a,b,end=" ")
    for i in range(num-2):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
---------------------------------------------------------------        

