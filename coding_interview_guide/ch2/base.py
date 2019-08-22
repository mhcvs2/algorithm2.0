

class Node(object):

    def __init__(self, value, n=None):
        self.value = value
        self.next = n


class DoubleNode(object):

    def __init__(self, value, n=None, l=None):
        self.value = value
        self.next = n
        self.last = l


class BaseUtils(object):

    @staticmethod
    def gen_single(data_list):
        if not data_list:
            return None
        head = Node(data_list[0])
        cur = head
        for data in data_list[1:]:
            next_node = Node(data)
            cur.next = next_node
            cur = next_node
        return head

    @staticmethod
    def to_list(head):
        res = []
        cur = head
        while cur is not None:
            res.append(str(cur.value))
            cur = cur.next
        return res

    @classmethod
    def print_single(cls, head):
        if not head:
            print('null')
            return
        data_list = cls.to_list(head)
        print(' -> '.join(data_list))

    @staticmethod
    def get_length(head):
        l = 0
        cur = head
        while cur is not None:
            cur = cur.next
            l += 1
        return l

    @staticmethod
    def is_equal(head1, head2):
        cur1 = head1
        cur2 = head2
        if cur1 is None and cur2 is None:
            return True
        while cur1 is not None or cur2 is not None:
            if cur1 is None or cur2 is None:
                return False
            if cur1.value != cur2.value:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True
