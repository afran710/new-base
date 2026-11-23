# class-blueprint
# object-real output

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

    def Bark(self):
        print(self.name,'says woof')

dog1=Dog('tom','beagle')
dog2=Dog('lucy',"pitbull")

dog1.Bark()
dog2.Bark()
