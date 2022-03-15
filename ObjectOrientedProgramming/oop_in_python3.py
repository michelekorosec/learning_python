class Dog: #Python class names in CapitalizedWords notation
    species = "Canis familiaris" #Class attribute

    def __init__(self,name,age, breed):
        #Instance attributes
        self.name = name
        self.age = age
        self.breed = breed


    def description(self):
        return f"{self.name} is {self.age} years old"


    def speak(self, sound):
        return f"{self.name} says {sound}"

    def __str__(self):
        return f"{self.name} is {self.age} years old"




miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

def class_and_instance_attributes():

    print(buddy.name)
    print(buddy.age)

    print(miles.name)
    print(miles.age)

    print(buddy.species)

    miles.species = "Felis silvestris"
    print(miles.species)

    return 0


def instance_methods():

    print(miles.description())

    print(miles.speak("Woof Woof"))
    print(miles.speak("Bow Wow"))

    print(miles)

    return 0

def check_understanding():

    class Car:

        def __init__(self, color, mileage):

            self.color = color
            self.milage = mileage

        def __str__(self):
            return f"The {self.color} car has {self.milage:,} miles"

    blue_car = Car("blue",20000)
    red_car = Car("red",30000)

    print(blue_car)
    print(red_car)

    return 0

def dog_park():

    print(buddy.speak("Yap"))
    print(jim.speak("Woof"))
    print(jack.speak("Woof"))


    return 0

def child_class():
    class Dog:
        species = "Canis familiaris"

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name} is {self.age} years old"

        def speak(self, sound):
            return f"{self.name} says {sound}"

    class JackRussellTerrier(Dog):
        pass

    class Dachshund(Dog):
        pass

    class Bulldog(Dog):
        pass

    miles = JackRussellTerrier("Miles", 4)
    buddy = Dachshund("Buddy", 9)
    jack = Bulldog("Jack", 3)
    jim = Bulldog("Jim", 5)

    print(type(miles))
    print(isinstance(miles,Dog))
    print(isinstance(miles,Bulldog))
    print(isinstance(jack,Dachshund))

    return 0

#class_and_instance_attributes()
#instance_methods()
#check_understanding()
#dog_park()
child_class()