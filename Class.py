class a(object):
    def __init__(self, name):
        self.name = name
        
    def getName(self):
        return self.name


aObject = a('bla')
print(aObject.getName())


class b(a):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        


bObject = b('ha', 24)
print(bObject.name)
print(bObject.age)


