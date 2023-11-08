num = int(input("Enter the number: "))

print("Multiplication Table of", num)
ran = int(input("Enter the range:"))

for i in range(1, ran):
    print(num, "X", i, "=", num * i)
