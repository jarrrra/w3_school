'''
while
'''
i = 1
while i < 6:
  print(i)
  i += 1 #always remember to increment

#break statement to finish the loop early
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue to skip to the next iteration
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else as an after-loop condition (not executed if break happens)
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

'''
for
'''
#with lists
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#with strings
for x in "banana":
  print(x)

#break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#with numbers range
for x in range(6):
  print(x)
#or
for x in range(2, 6):
  print(x)
#or
for x in range(2, 30, 3):
  print(x)

#else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#pass for loops that do nothing
for x in [0, 1, 2]:
  pass
