def isPalindrome(head:list) -> bool:
    q:list = []

    if not head:
        return True
    
    node = head

    #리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

     