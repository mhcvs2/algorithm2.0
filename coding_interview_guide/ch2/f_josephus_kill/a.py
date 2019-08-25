# encoding: utf-8


def josephus_kill(head, m):
    if head is None or head.next == head or m < 1:
        return head
    # 环形找一个节点的前置节点
    pre = head
    while pre.next is not head:
        pre = pre.next
    count = 0
    while head is not pre:
        count += 1
        if count == m:
            pre.next = pre.next.next
            count = 0
        else:
            pre = pre.next
        head = pre.next
