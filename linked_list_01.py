# 함수 구현
class Node(): #node 라는 이름의 클래스 생성
    def __init__(self): #생성자
        self.data = None
        self.link = None
        
        
# 변수


# 메인
node1 = Node()
node1.data = '다현'
node1.data

node2 = Node()
node2.data = '정연'
node1.link = node2 #node1 의 링크가 node2를 가르킨다

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

node1.data
node1.link.data
node1.link.link.data
node1.link.link.link.data
node1.link.link.link.link.data

# 많이 쓰이고 중요한 코드 
# 스스로 짤 수 있어야 한다 
current = node1
print(current.data)
# 마지막이 아니면 == 링크가 비어있지 않으면 
while current.link != None :
    current = current.link
    print(current.data, end=' ')


# 그림보고 복습
current = node1
print(current.data)
while current.link != None:
    current = current.link #그다음 링크로 연결
    print(current.data,end=' ')
