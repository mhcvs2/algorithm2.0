

class PetEnterQueue(object):

    def __init__(self, pet, count):
        self._pet = pet
        self._count = count

    @property
    def pet(self):
        return self._pet

    @property
    def count(self):
        return self._count

    @property
    def enter_pet_type(self):
        return self.pet.type


class DogCatQueue(object):

    def __init__(self):
        self._dog_queue = []
        self._cat_queue = []
        self._count = 0

    def add(self, pet):
        if pet.type == "dog":
            self._dog_queue.append(PetEnterQueue(pet=pet, count=self._count))
            self._count += 1
        elif pet.type == "cat":
            self._cat_queue.append(PetEnterQueue(pet=pet, count=self._count))
            self._count += 1
        else:
            raise Exception("err, not dog or cat")

    def poll_all(self):
        if len(self._dog_queue) > 0 and len(self._cat_queue) > 0:
            if self._dog_queue[-1].count > self._cat_queue[-1].count:
                return self._cat_queue.pop().pet
            else:
                return self._dog_queue.pop().pet
        elif len(self._dog_queue) > 0:
            return self._dog_queue.pop().pet
        elif len(self._cat_queue) > 0:
            return self._cat_queue.pop().pet
        else:
            raise Exception("queue is empty")

    def poll_dog(self):
        if len(self._dog_queue) > 0:
            return self._dog_queue.pop().pet
        else:
            raise Exception("dog queue is empty")

    def poll_cat(self):
        if len(self._cat_queue) > 0:
            return self._cat_queue.pop().pet
        else:
            raise Exception("cat queue is empty")

    @property
    def is_empty(self):
        return len(self._dog_queue) == 0 and len(self._cat_queue) == 0

    @property
    def is_dog_empty(self):
        return len(self._dog_queue) == 0

    @property
    def is_cat_empty(self):
        return len(self._cat_queue) == 0
