a=int(input(" intake of calories "))
b= float(input("how much percentage you want to increase"))
c= int(input("How many days you want to calculate"))

i=1
while(i<=c):
    a=a+a*(b/100)
    print(f"Day{i}-",a)
    i=i+1


d=int(input("intake of calories"))
e= float(input("decreasing percentage"))
f= int(input("How many days you want to calculate"))

i=1
while(i<=f):
    d=d-d*(b/100)
    print(f"Day{i}-",d)
    i=i+1    