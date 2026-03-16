from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)
def solution(nodeinfo):
    number = defaultdict(int)

    for i in range(len(nodeinfo)):
        number[tuple(nodeinfo[i])] = i+1
    
    nodeinfo.sort(key=lambda x: (-x[1], x[0])) # y좌표 내림차순, x좌표 오름차순 정렬
    
    class Node:
        def __init__(self, x, y, num):
            self.x = x
            self.y = y
            self.num = num
            self.left = None
            self.right = None
    
    root = Node(nodeinfo[0][0], nodeinfo[0][1], number[tuple(nodeinfo[0])]) # root node
    
    def insert_tree(parent, child):
        if child.x < parent.x:
            if parent.left == None:
                parent.left = child
            else:
                insert_tree(parent.left, child)
        else:
            if parent.right == None:
                parent.right = child
            else:
                insert_tree(parent.right, child)
    
    for i in range(1, len(nodeinfo)):
        cur_node = Node(nodeinfo[i][0], nodeinfo[i][1], number[tuple(nodeinfo[i])])
        insert_tree(root, cur_node)
    
    preorder, postorder = [], []
    
    def preorder_traverse(node):
        if node:
            preorder.append(node.num)
            preorder_traverse(node.left)
            preorder_traverse(node.right)
    
    def postorder_traverse(node):
        if node:
            postorder_traverse(node.left)
            postorder_traverse(node.right)
            postorder.append(node.num)
    
    preorder_traverse(root)
    postorder_traverse(root)
    
    answer = [preorder, postorder]
    
    
    return answer