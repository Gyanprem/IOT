sub1 = int(input("Enter marks sub1 : "))
sub2 = int(input("Enter marks sub2 : "))
sub3 = int(input("Enter marks sub3 : "))
avg = (sub1+sub2+sub3)/3
if (avg >= 90) and (avg <= 100):
    print("grade A")
elif(avg >= 80) and (avg <= 89):
    print("grade B")
elif(avg >= 70) and (avg <= 79):
    print("grade C")
elif(avg >= 60) and (avg <= 69):
    print("grade D")
else:
    print("grade F")
