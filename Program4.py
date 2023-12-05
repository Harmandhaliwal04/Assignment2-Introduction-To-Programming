myNumbers=[500,600,800,100,50,250,445,666,1400]
for i in range(0,8):
 
    print(myNumbers[i])

y=myNumbers[7]
myNumbers[7]=myNumbers[8]
myNumbers[8]=y
print(myNumbers)
myNumbers.sort(reverse=True)
print(myNumbers)

