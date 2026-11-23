class dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(self.name,"says woof!")
# object
dog1=dog('rocky','beagle')
dog2=dog('lucy','pitbull')

dog1.bark()
dog2.bark()