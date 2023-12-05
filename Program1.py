a=int(input("Enter Number of years  "))
total=0
i=1
c=a*12
while(i<=c):
    b=float(input(f"Enter  average temperature of  Month {i} "))
    i=i+1
    total=total+b
print("The Average High Temperature",total)  
average=total/c
print("Temperture",average)

