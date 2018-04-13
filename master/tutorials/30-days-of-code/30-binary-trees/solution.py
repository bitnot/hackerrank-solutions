    def levelOrder(self,root):
        if not root: 
            return
        from collections import deque
        q = deque([root])
        while deque:
            curr = q.popleft()
            print(curr.data, end = " ")
            if curr.left: 
                q.append(curr.left)
            if curr.right: 
                q.append(curr.right)