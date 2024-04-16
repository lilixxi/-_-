### 함수 ###
class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

### 변수 ###

### 메인 ###
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right = node5

node6 = TreeNode()
node6.data = '선미'
node3.left = node6

print(node1.data,node2.data,node3.data,end=' ')
print(node4.data,node5.data,node6.data,end=' ')
# 이렇게 접근하지보다는,, 모든 데이터는 루트에 연결됨 -> 루트로 접근 
root = node1
print(root.data,root.left.data,root.right.data,end=' ')
print(root.left.left.data,root.left.right.data,root.right.left.data,end=' ')