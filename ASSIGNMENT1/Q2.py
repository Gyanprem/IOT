num1 = int(input("Enter number : "))
print(f"num1 = {num1}")
temp=num1
d=num1%10
num1=num1/10
c=num1%10
num1=num1/10
b=num1%10
num1=num1/10
a=num1
print(f"{a ,b ,c ,d}")
print(f"temp={a*1000}{b*100}{c*10}{d}")
print(f"{d,c,b,a}")