'''
creation
'''
#how to create (can have different types inside)
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
#or
thisdict = dict(name = "John", age = 36, country = "Norway")

'''
items, keys, values
'''
#accessing an item from dictionary
x = thisdict["model"]
x = thisdict.get("model")

#accessing keys list
x = thisdict.keys()

#accessing values list
x = thisdict.values()

#accessing items as a list of tuples (key, value)
x = thisdict.items()

#finding and printing length of the dictionary
print(len(thisdict))

'''
manipulations of items
'''
#checking if a key exists
if "model" in thisdict:
  print("Yes")

#changing value
thisdict["year"] = 2018

#adding new value
thisdict["color"] = "blue"

#using method update() to change..
thisdict.update({"year": 2020})
#..or add a key and its value
thisdict.update({"most sold in color": "red"})

#removing from dictionary
thisdict.pop("model")
thisdict.popitem() #last inserted
del thisdict["model"] #or del thisdict to delete the whole dictionary
thisdict.clear() #to clean all values

'''
looping through dictionaries
'''
#looping through keys
for x in thisdict: #the same behavior would be with thisdict.keys()
  print(x) #prints keys
  print(thisdict[x]) #prints values

#a way to loop directly through values
for x in thisdict.values():
  print(x)

#to loop through both values and keys
for x, y in thisdict.items():
  print(x, y)

'''
copying dictionaries
'''
mydict = thisdict.copy()
mydict = dict(thisdict)

'''
nested dictionaries
'''
#creating
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#or
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

#accessing items
print(myfamily["child2"]["name"])

#looping
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
