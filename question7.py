# 13021326

""" Provide the implementation of three classes Person, Adult, Child that fulfills the
following requirements. First, the classes must have the constructors as below:
class constructor functionality
Person sets the two given strings as the first and last names
Adult sets the two given strings as the first and last names,
and the third given string as the phone number
Child sets the two given strings as the first and last names,
and the two given Person objects as first and second parents
Second, the following methods must be present:
class method name functionality
Person get_info returns a string containing the first and the last names
separated by space
get_name returns a tuple containing the strings of the first and last name
Adult get_info same as get_info for Person above
get_name same as get_name for Person above
get_phone returns the phone number as a string
Child get_info returns a string containing the first and last names of the child,
then first and last names of first parent,
then first and last names of second parent,
all words separated by space
get_name same as get_name for Person above
get_parents returns a tuple of two Person objects, where
the first element is first parent and the second is second parent
Brevity, minimal repetition of code, and use of inheritance, is important for marking.
Provide full implementation of the three classes, their methods and constructors. For
any of the classes, do NOT provide methods or constructors other than listed above.
Indicative test cases:
p = Person("Mary", "Ann")
a = Adult("John", "Doe", "1234567")
c = Child("Richard", "Doe", p, a)
assert a.get_info()== "John Doe" #must be True
assert c.get_name()==("Richard", "Doe") #must be True
assert c.get_info()== "Richard Doe Mary Ann John Doe" #must be True
assert c.get_parents() == (p,a) #must be True """

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return "" + self.first_name + " " + self.last_name

    def get_name(self):
        f = str(self.first_name)
        l = str(self.last_name)
        name = (f, l)
        return name

class Adult(Person):
    def __init__(self, first_name, last_name, phone_num):
        super().__init__(first_name, last_name)
        self.phone_num = phone_num

    def get_phone(self):
        return str(self.phone_num)


class Child(Person):
    def __init__(self, first_name, last_name, parent1, parent2):
        super().__init__(first_name, last_name)
        self.parent1 = parent1
        self.parent2 = parent2

    def get_info(self):
        name = super().get_info()
        p1 = self.parent1.get_info()
        p2 = self.parent2.get_info()
        return name + " " + p1 + " " + p2

    def get_parents(self):
        parents = (self.parent1, self.parent2)
        return parents




# Indicative test cases:
p = Person("Mary", "Ann")
a = Adult("John", "Doe", "1234567")
c = Child("Richard", "Doe", p, a)
assert a.get_info()== "John Doe" #must be True
assert c.get_name()==("Richard", "Doe") #must be True
assert c.get_info()== "Richard Doe Mary Ann John Doe" #must be True
assert c.get_parents() == (p,a) #must be True