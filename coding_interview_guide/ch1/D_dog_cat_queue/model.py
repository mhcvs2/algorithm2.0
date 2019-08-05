

class Pet(object):

    def __init__(self, pet_type):
        self._type = pet_type

    @property
    def type(self):
        return self._type


class Dog(Pet):

    def __init__(self):
        super(Dog, self).__init__("dog")


class Cat(Pet):

    def __init__(self):
        super(Cat, self).__init__("cat")
