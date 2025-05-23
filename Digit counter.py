num = int(input("Enter a number: "))
d=0
n=num
while n>0:
    d+=1
    n=n//10
print(num,' is a ',d,' digit number')
