x = 'almost'
y = ' weekend'
x + y

'''Function definition and invocaton''' # Documentation 
def happyCodingWithPython():
	print("Python supports Imperative programming")
	print("Python supports Functional programming")
	print("Python supports Object-oriented programming")
	print("... and more")
	print()

x = 5 + 2j

fun_languages = ['Python', 'JS', 'Eiffel', 'Ada']
cool_paradigms = ["Functional", "Object-Oriented"]

i = 0
for lang in fun_languages:
	i = i + 1
	print(i, lang)
print()

j = 0
while j < len(fun_languages):
	langl = fun_languages
	print(langl[j])
	j += 1
print()

def add(x, y):
	if x == 0: return y
	else: return add(x - 1, y + 1)

sandwich_price = [(2014, 25.05), (2015, 26.03), (2016, 25.12), (2017, 25.02), (2018, 24.08)]
max(sandwich_price) #(2018, 24.08)
max(sandwich_price, key = lambda sprice: sprice[1]) #(2015, 26.03)

listValues = [2014, 2015, 2016, 2017, 2018]
addOne = list(map(lambda y: y + 1, listValues)) 
print(addOne) #[2015, 2016, 2017, 2018, 2019]

#OBS!
#addOne = map(lambda y: y + 1, listValues) #<map object at 0x03210FD0>

listValues2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
filterEven = list(filter(lambda y: y%2==0, listValues2)) #[2, 4, 6, 8, 0]
filterOdd = list(filter(lambda y: y%2==1, listValues2)) #[1, 3, 5, 7, 9]

def main(): # Not real main; Read about it! 
	happyCodingWithPython()
	
	print(add(2, 3))
	print()

main()

# 16.11.2018 OO Programming in Python #

class Person:
    def __init__(self, name): # !!!OBS!!! Double underscore !!!
        self.name = name
        print(self.name)

#person1 = Person('Max Mustermann')
#Max Mustermann

class SEViaStud:
    where = 'VIA' # One can use "location" instead of "where"
    def __init__(self):
        self.where = 'VIA-Horsens'

#print(SEViaStud.where)
#VIA
#print(SEViaStud().where)
#VIA-Horsens

# Inheritance
class Person2:
    def speak(self): 
        print('I can speak FSharp, Scala and now Python')

class Student(Person2):
    def watch(self):
        print('I like to watch comedy films')

class Staff(Person2):
    def watch(self):
        print('I like to watch romantic films')

#stud2 = Student()
#stud2.speak()
#I can speak FSharp, Scala and now Python
#stud2.watch()
#I like to watch comedy films

# Multiple inheritance
class Contact:
    allContacts = [] #additional line
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.allContacts.append(self) #additional line

class MailSender:
    def sendMail(self, message): # e-mail sending logic
        print(message)
        print("Sending: (" + message + ")")

class EmailableContact(Contact, MailSender):
    pass # just runs the code that I have / ignores..

#emc = EmailableContact("Peter Adams", "pa@happytreefriends.org")
#emc.sendMail("Dinner is ready")
#Dinner is ready
#Sending: (Dinner is ready)

# Polymorphism (in practice I)
class Animal:
    def name(self): 
        print('My name is') # or pass and give it a name in the subclass
    def makeASound(self):
        print('Make a sound') # or pass (more logical here because animal)
    def sleep(self):
        print('Sleeping...') 

class Cow(Animal):
    def name(self):
        print('I am a cow') # Both '' and "" allowed
    def makeASound(self):
        print('Moooo')

class Cat(Animal):
    def name(self):
        print('I am a cat') 
    def makeASound(self):
        print('Meeeoow')

class Dog(Animal):
    def name(self):
        print('I am a dog')
    def makeASound(self):
        print("Woooow")

#Cow1 = Cow()
#Cow1.makeASound()
#Moooo
#Cow1.name()
#I am a cow
#Cow1.sleep()
#Sleeping...

class TestAnimals:
    def printNames(self, animal):
        animal.name()
    def gotoSleep(self, animal):
        animal.sleep()
    def makeSound(self, animal):
        animal.makeASound()

MyCow = Cow()
MyCat = Cat()
MyDog = Dog()

Testing = TestAnimals()

Testing.gotoSleep(MyCow)
Testing.gotoSleep(MyCat)
Testing.gotoSleep(MyDog)

Testing.makeSound(MyCow)
Testing.makeSound(MyCat)
Testing.makeSound(MyDog)

Testing.printNames(MyCow)
Testing.printNames(MyCat)
Testing.printNames(MyDog)

#Testing.gotoSleep(MyCow)
#Sleeping...
#Testing.gotoSleep(MyCat)
#Sleeping...
#Testing.gotoSleep(MyDog)
#Sleeping...
#Testing.makeSound(MyCow)
#Moooo
#Testing.makeSound(MyCat)
#Meeeoow
#Testing.makeSound(MyDog)
#Woooow
#Testing.printNames(MyCow)
#I am a cow
#Testing.printNames(MyCat)
#I am a cat
#Testing.printNames(MyDog)
#I am a dog
