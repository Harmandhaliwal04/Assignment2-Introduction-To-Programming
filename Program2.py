a=int(input(" Starting daily calorie intake"))
b= float(input("Average daily percentage decrease"))
c= int(input("The number of days"))

i=1
while(i<=c):
    a=a-a*(b/100)
    print(f"Day{i}-",a)
    i=i+1


if a<1200:
    print("diet stabilized")

  
 