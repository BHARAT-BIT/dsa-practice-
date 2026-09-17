def lca(root,p,q):
    if root is None:
        return None 

    if root == p or root ==q:
        return root 
    leftlca = lca(root.left,p,q)
    rightlca = lca(root.right,p,q)

    if leftlca and rightlca:
        return root 
    elif leftlca:
        return leftlca 
    return rightlca 