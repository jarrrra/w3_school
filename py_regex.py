import re

#search

txt = "The rain in Spain"
x = re.search("\s", txt)

print(x.span())
print("The first white-space character is located in position:", x.start())
print(x.string)
print(x.group())

#findall

x = re.findall("ai", txt)
print(x)

#split

x = re.split("\s", txt, 1) #the last parameter can be omitted if we need to split for all occurences
print(x)

#sub (replace)

x = re.sub("\s", "9", txt, 2) #the last one is the same as for split
print(x)
