def bst_min(top):
    min = top
    while min.left is not None:
        min = min.left
    return min

def bst_max(top):
    max = top
    while max.right is not None:
        max = max.right;
    return max