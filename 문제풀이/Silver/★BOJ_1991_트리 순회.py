# 트리 순회
n = int(input()) # n은 최대 26
tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0]) # 왼쪽
        preorder(tree[root][1]) # 오른쪽

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # 왼쪽
        print(root, end='')
        inorder(tree[root][1]) # 오른쪽

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0]) # 왼쪽 자식
        postorder(tree[root][1]) # 오른쪽 자식
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
