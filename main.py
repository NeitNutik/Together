import classes
test = classes.Cat("Bobik", "Cat")
test1 = classes.Dog("Sharik", "Dog")
test2 = classes.Dog("King", "Cow")

class Animal(classes.Cat,classes.Dog,classes.Cow):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

print(test.name,test.sound,test1.name,test1.sound,test2.name,test2.sound)