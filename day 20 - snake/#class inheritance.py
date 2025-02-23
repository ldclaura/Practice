#class inheritance
#chef class
#pastry chef class
#pastry chef inherits from chef so that you dont have to repeat yourself, adds more functions like bake.

#inherit appearance
#inherit behaviour

#class Animal:
    #def __init__(self):
        #self.num_eyes = 2
    #def breathe(self):
        #print("Inhale exhale")


#class Fish(Animal):
    #def __init__(self):
        #super().__init__()
    #def swim(self):
        #print("Swim")

#the superclass is the Animal, it inherits from the superclass with the super().__init__()
#nemo = Fish()
#nemo.swim() "Swim"
#nemo.breathe() "Inhale exhale"
#print(nemo.num_eyes) 2

#----------------------------------------------

#class Fish(Animal):
    #def __init__(self):
        #super().__init__()
    #def breathe(self):
        #super().breathe()
        #print("doing this underwater")
    #def swim(self):
        #print("Swim")

#super().breathe() makes it run the breathe function from the superclass (Animal), so you can add more things the func does after.
#nemo = Fish()
#nemo.swim() "Swim"
#nemo.breathe() "Inhale exhale" "doing this underwater"
#print(nemo.num_eyes) 2