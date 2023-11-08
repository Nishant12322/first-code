lower_value = int(input("Enter the lowervalue: "))
higher_value = int(input("Enter the highervalue: "))
print("the Prime numbers:")
for number in range(lower_value, higher_value+1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
