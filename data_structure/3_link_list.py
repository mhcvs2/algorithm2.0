

class Node(object):

    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    def __str__(self):
        return self.data
