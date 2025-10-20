class ListNode:
    def __init__(self, value: int, next = None):
        self.val = value
        self.next = next
    def __repr__(self):
        return f"ListNode(val={self.val})"


def main(lists):
    while len(lists) > 1:
        merge_l = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None
            # print('i:',i, ',l1:',PrintLinkedList(l1), ',l2:',PrintLinkedList(l2))
            merge_l.append(MergeTwoLists(l1, l2))
            # print('after merge:')
            # print('i:',i, ',l1:',PrintLinkedList(l1), ',l2:',PrintLinkedList(l2))
        lists = merge_l
    return lists[0]

    
def MergeTwoLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val > l2.val:
            cur.next = l2
            l2 = l2.next
        else:
            cur.next = l1
            l1 = l1.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next

def PrintLinkedList(head):
    cur = head
    arr = []
    while cur:
        arr.append(str(cur.val))
        cur = cur.next
    print(' -> '.join(arr)+' -> None')

# lists = [ListNode(1, ListNode(4, ListNode(5))), 
#          ListNode(1, ListNode(3, ListNode(4))), 
#          ListNode(2, ListNode(6))]

lists = [
    ListNode(1, ListNode(10)),
    ListNode(2),
    ListNode(3, ListNode(4, ListNode(5)))
]
PrintLinkedList(main(lists))