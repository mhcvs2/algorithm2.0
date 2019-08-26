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


# 老编号=(新编号+m-1)%i+1
# m是要删除第m个节点
# i是当前环形链表的节点数


def josephus_kill2(head, m):
    if head is None or head.next == head or m < 1:
        return head
    # 求节点数
    cur = head
    n = 0
    while cur.next is not head:
        n += 1
        cur = cur.next
    live_n = get_live(n, m)
    live_n -= 1
    while live_n != 0:
        live_n -= 1
        head = head.next
    head.next = head
    return head


def get_live(i, m):
    if i == 1:
        return 1
    return (get_live(i-1, m) + m - 1) % i + 1
