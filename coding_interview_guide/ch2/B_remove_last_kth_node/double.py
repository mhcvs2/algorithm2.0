

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
        res = head.next
        res.last = None
        return res
    cur = head
    k += 1
    while k < 0:
        cur = cur.next
        k += 1
    next_node = cur.next.next
    cur.next = next_node
    if next_node is not None:
        cur.next.next.last = cur
