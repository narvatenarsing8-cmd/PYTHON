a = int(input("enter n"))
count = 0
while a > 0:
    count = count + 1
    a = a / 10
    print("sum of digits=",count)