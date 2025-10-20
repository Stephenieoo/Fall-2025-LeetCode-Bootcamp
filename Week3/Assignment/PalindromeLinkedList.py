class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def main(head) -> bool:
    # find the middle of linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    
    

    
    # reverse the second part of linked list


def PrintLinkedList(head):
    if not head:
        print('None')
    arr = []
    while head:
        arr.append(str(head.val))
        head = head.next
    return ' -> '.join(arr) + ' -> None'

head = [1,2,2,1]
PrintLinkedList()
