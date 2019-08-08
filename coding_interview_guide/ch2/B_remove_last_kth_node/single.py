

class Node(object):

    def __init__(self, value, n=None):
        self.value = value
        self.next = n


def remove_last_kth_node(head, k):
    if head is None or k < 1:
        return head
    cur = head
    while cur is not None:
        k -= 1
        cur = cur.next
    if k > 0:
        return head
    if k == 0:
        return head.next
    cur = head
    k += 1
    while k < 0:
        cur = cur.next
        k += 1
    cur.next = cur.next.next
