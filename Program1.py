x=int(input("Enter Number of years  "))
total=0
i=0
z=x*12
while(i<=z):
    y=float(input("The average high temperature  "))
    i=i+1
    total=total+y
print("The Average High Temperature",total)  
average=total/z
print("Temperture",average)