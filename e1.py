#ask yser to input 3 numbers and you have to print average of three number using string formattting
#Bonus try to take all three comma separated inputs in one line

a, b, c=input("enter number comma separated").split(",")
print(a)
print(b)
print(c)
print(int(a)+int(b)+int(c)/3)
print (f"the avg for number{int(a)+int(b)+int(c)/3}")