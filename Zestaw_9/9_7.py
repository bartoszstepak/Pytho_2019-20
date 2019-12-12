def bst_min(top):
    if top is None:
        rise ValueError("Three is empty");
        
    min = top
    
    while min.left is not None:
        min = min.left
        
    return min


def bst_max(top):
    if top is None:
        rise ValueError("Three is empty");
    
    max = top
    
    while max.right is not None:
        max = max.right;
    
    return max
