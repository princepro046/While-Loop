#ArmStrong Numbers 

num = int(input("Enter a Number :"))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    digit = digit ** 3
    sum = sum + digit
    temp = temp // 10

    #display the result
    if num == sum:
        print(num,"is an Armstrong Number")
else:
    print(num,"is not an Armstrong Number")
