#creating class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  def myfunc(self):
    print("Hello my name is " + self.name)
    
#we can use different name other than self to do function on a different object
  def newfunc(abc): 
    return abc.age + 1

  def anotherfunc(self):
    pass #to have an empty func

#class that inherits from Person
class Student(Person):
  #inheriting function from parent
  def __init__(self, name, age):
    super().__init__(name, age)
    self.graduationyear = 2019 #adding new attributes

  #we can rewrite functions
  def myfunc(self):
    print("Hello my name is " + self.name + " and I am a student")


#creating objects
p1 = Person('John', 40)
p2 = Student('John', 18)

#using functions of objects
p1.myfunc()
p2.myfunc()

#deleting attribute name and then the whole object
del p1.age
del p1
