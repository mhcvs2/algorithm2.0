

class EmptyError(Exception):
    pass


class GetMinStack2(object):

    def __init__(self):
        self._data_stack = []
        self._min_stack = []

    def push(self, item):
        self._data_stack.append(item)
        if len(self._min_stack) == 0 or item <= self._min_stack[-1]:
            self._min_stack.append(item)
        else:
            self._min_stack.append(self._min_stack[-1])

    def pop(self):
        self._check_empty()
        self._min_stack.pop()
        return self._data_stack.pop()

    def get_min(self):
        self._check_empty()
        return self._min_stack[-1]

    def _check_empty(self):
        if len(self._data_stack) == 0:
            raise EmptyError()
