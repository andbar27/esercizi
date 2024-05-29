# [1,2,3,5,6,7]
# elemento in pos. 0 (1) -> radice
# per l'elemento in pos i -> il figlio a sinistra si trova in pos. 2*i + 1
# per l'elemento in pos i -> il filgio a destra si trova in pos. 2*(i + 1) = 2*i + 2
#       1
#    /      \
#   2         2
# /   \      /  \
# 4   5     5    4
#      \   /
#      6   6
def is_symmetric(tree: list[int]) -> bool:
    return are_mirrored(tree, 1, 2)

def are_mirrored(tree, left_index, right_index) -> bool:
    
    if left_index >= len(tree) and right_index >= len(tree):
        return True
    elif (left_index >= len(tree) and right_index < len(tree))\
          or (left_index < len(tree) and right_index >= len(tree)):
        return False

    if tree[left_index] != tree[right_index]:
        return False
    
    left_of_left = 2 * left_index + 1
    right_of_left = 2 * left_index + 2

    left_of_right = 2 * right_index + 1
    right_of_right = 2 * right_index + 2

    is_symmetric_external: bool = are_mirrored(tree, left_of_left, right_of_right)
    is_symmetric_internal: bool = are_mirrored(tree, right_of_left, left_of_right)

    return is_symmetric_internal and is_symmetric_external



def is_symmetric_luca(tree: list[int]) -> bool:
    tree_dict: dict[str, list[int]] = {}
    tree_dict['0-a'] = [tree[1]]
    tree_dict['0-b'] = [tree[2]]

    for i in range(1, len(tree) // 2):
        if 2 * (i + 1) < len(tree):
            tree_dict[f'{i}-a'] = [tree[2*i+1], tree[2*(i+1)]]
            tree_dict[f'{i}-b'] = [tree[2*(i+1)+1], tree[2*((i+1)+1)]]

    for i in range(len(tree_dict) // 2):

        if tree_dict[f'{i}-a'] != list(reversed(tree_dict[f'{i}-b'])):
            return False
    
    return True



class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric_with_class(root: TreeNode) -> bool:

    def are_mirrored(left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        is_symmetric_external: bool = are_mirrored(left.left, right.right)
        is_symmetric_internal: bool = are_mirrored(left.right, right.left)

        return is_symmetric_external and is_symmetric_internal
    
    return are_mirrored(root.left, root.right)

def build_tree(tree: list[int]) -> TreeNode:
    # tree = [1,2,3,None,4,None,5]
    nodes = []
    for val in tree:
        if val:
            nodes.append(TreeNode(val))
        else:
            nodes.append(None)
    # figlio a sinistra sta in 2*i+1
    # figlio a destra sta in 2*i+2
    for i in range(len(nodes) // 2):
        if nodes[i]:
            left_index = 2*i + 1
            right_index = 2*i + 2
            if left_index < len(nodes):
                nodes[i].left = nodes[left_index]
            if right_index < len(nodes):
                nodes[i].right = nodes[right_index]
    return nodes[0]
    
def is_symmetric_v1(tree: list[int]) -> bool:
    root = build_tree(tree)
    return is_symmetric_with_class(root)

tree = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3,left=TreeNode(4),right=TreeNode(4)), 
                                     right=TreeNode(val=3,left=TreeNode(4),right=TreeNode(4))), 
                        right=TreeNode(val=2,left=TreeNode(3,left=TreeNode(4),right=TreeNode(4)),
                                                    right=TreeNode(3,left=TreeNode(4),right=TreeNode(4))))

print(is_symmetric_with_class(tree))
ltree = [1,2,2,3,3,3,3,4,4,4,4,4,4,4,4,
         5,5,5,3,5,5,5,5,5,5,5,5,3,5,5,5]
print(is_symmetric(ltree))