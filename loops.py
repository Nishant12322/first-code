#loops
a = 33
b = 200

if b > a:
  print("b is greater than a")

a = 22
b = 22
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
a = 200
b = 30
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
a = 200
b = 33
if b > a:
 print("b is greater than a")
else:
  print("b is not greater than a")

a = 33
b = 200
if a < b: print("a is greater than b")

if a > b: print("a is greater than b") #short handed if
  
a = 200
b = 36

print("A") if a > b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#nested if
x = 55
if x < 10:
  print("Above 20,")
  if x > 20:
    print("and also above 30!")
  else:
    print("but not above 20.")
    
  a = 33
  b = 200
  if b > a:
   pass
 
    





