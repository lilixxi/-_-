# 연결된 리스트 실무코드

############
# 함수선언 #
class Node():
    def __init__(self):
        self.data = None
        self.link = None

#############        
# 출력 
def printNodes(start):
    current = start # 첫 부분 부터 시작 
    print(current.data,end=' ')
    while current.link != None:
        current = current.link #그다음 링크로 연결
        print(current.data,end=' ')

        
###############
# 삽입
def insertNode(find_data,insert_data):
    global head,pre,current #전역변수로 만들어주기 
    # case 1 : 첫노드에 일경우
    if find_data == head.data :
        node = Node()
        node.data = insert_data
        node.link = head
        head = node
        
    # case2 : 중간노드일 경우  
    current = head 
    while current.link != None : #마지막이 아닐때까지 
        current = current.link # current 위치변경
        if current.data == find_data :
            node = Node()
            node.data = insert_data
            # current , pre 가 쌍으로 이동해야함 
            node.link = current 
            pre.link = node 
            # case3 :  마지막일 경우
            node = Node()
            node.data = insert_data
            current.link = node
            return
    printNodes(head)
 
###############   
# 삭제 
def deleteNode(delete_data) :
    global head,pre,current #전역변수로 만들어주기 
    # case1 : 첫 노드 일 경우
    if delete_data == head.data : 
        current = head 
        head = head.link # head를 다음으로 옮긴다
        del current # current 를 제거 
        return 

    # case2 : 중간 노드 일 경우
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == delete_data :
            pre.link = current.link
            del current
            return
    # case3 : 없는노드 삭제
    else : return # 할게 없음
 
    printNodes(head)   
    
###############
# 노드검색
def findNode(find_data):
    global head,pre,current
    current = head
    if current.data == find_data :
        return current
    
    while current.link != None :
        current = current.link
        if current.data == find_data :
            return current
    
    return Node() # 그냥 리턴해도 되지만 리턴되는 값을 맞춰준다 / 빈노드를 리턴




###############   
# 변수선언 #
memory = []
head,pre,current = None,None,None # 변수 지정
# head : 첫 노드
# current : 현재 작업중인 노드
# pre : 현재 작업중인것 바로 앞노드 / 나의 바로 앞을 알아야 삽입,삭제 가능
dataArray = ['다현','정연','쯔위','사나','지효']


###############
# 메인코드 #
# 변수 재사용을 위해 node 라 쓰기 
node = Node()
node.data = dataArray[0]
head = node


# 첫 노드는 헤드를 위해 따로 처리해도, 나머지 코드는 반복문으로 처리하자
for data in dataArray[1:]:
    # 노드 재사용 전 지정 
    pre = node 
    node = Node()
    node.data = data #새로운 데이터 넣고
    pre.link = node #지금의 노드를
printNodes(head)

# 첫 노드 삽입
insertNode('다현','화사')
# 중간 노드 삽입
insertNode('사나','휘인')
# 마지막 노드 삽입
insertNode('재남','문별')
# 재남이 없음 -> 재남의 위치가 아닌 새 노드를 생성하고 마지막 삽입

# 삭제 
deleteNode('화사')
deleteNode('정연')
deleteNode('재남') # 없는것을 지우라 

retNode = findNode('사나')
retNode = findNode('가희')
print(retNode.data,'의 뮤직비디오가 플레이 됩니다')

