#num=int(input("Enter the numer"))
#print (" Prime numbers ", num)

num=11
if num > 3:
    for i in range (2 ,int(num/2)+1):
        if (num % i)== 0:
            print (num,"It is not a prime number")
            break
        else:
          print (num, "It is a prime number")
else:
    print (num,"It is not a prime number")
    

