class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

'''
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

'''

def main(head):
    # base case:
    if not (head and head.next):
        return head

    # find the middle node
    # odd:  2 3 4 5 6   slow = 4
    # even: 2 3 4 5     slow = 4
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # save the slow next
    cur = slow.next
    
    # cut from middle
    slow.next = None

    # reverse the list from cur
    prev = None
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node

    # merge the two lists
    n1, n2 = head, prev
    dummy = ListNode(0)
    cur = dummy
    while n1 and n2:
        cur.next = n1
        n1 = n1.next
        cur = cur.next
        cur.next = n2
        n2 = n2.next
        cur = cur.next
    
    # insert the rest
    cur.next = n1 if n1 else n2
    return dummy.next

def PrintListNode(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(' -> '.join(res) + ' -> None')

list1 = ListNode(1, ListNode(2, ListNode(3,ListNode(4))))
list2 = ListNode(1, ListNode(2, ListNode(3,ListNode(4, ListNode(5)))))

# PrintListNode(list1)

PrintListNode(main(list1))
PrintListNode(main(list2))