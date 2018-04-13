def check_binary_search_tree_(root):
    def check(node,minv,maxv):
        return node == None or (
            minv < node.data < maxv and check(node.left, minv, node.data) and check(node.right,node.data,maxv))
    return check(root,0,10000)