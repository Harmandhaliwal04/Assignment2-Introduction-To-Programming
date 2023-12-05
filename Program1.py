a=int(input("Enter Number of years  "))
total=0
i=0
c=x*12
while(i<=c):
    y=float(input("The average high temperature  "))
    i=i+1
    total=total+y
print("The Average High Temperature",total)  
average=total/c
print("Temperture",average)