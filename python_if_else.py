#if..elif..else. examples
a = 33
b = 200
if b > a:
  print("b is greater than a") #must have correct indentation

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#can have else without elif
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#shortened, one-line versions
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#logic operators in conditions
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement when condition does nothing
a = 33
b = 200

if b > a:
  pass

