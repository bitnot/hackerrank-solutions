def rel_height(node, node_height):
    return max(
        node_height, 
        rel_height(node.left, node_height + 1), 
        rel_height(node.right, node_height + 1)
    ) if node else 0

def height(root):
    return rel_height(root, 0)