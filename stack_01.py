## 함수 ##

## 변수 ##
stack = [None,None,None,None,None] #5칸짜리 빈스택 생성
top = -1  #stack 초기화



## 메인 ##

# 1. push 
# 초기값 top 설정 
# top 을 한칸 위로 이동
# top 위치에 데이터 입력 (push)
top += 1 
stack[top] = 'coffee'
top += 1
stack[top] = 'green tea'
top += 1
stack[top] = 'honey water'
print('bottom =>', stack, '=> top')

# 2. pop 
# top 의 위치에 있는 데이터 추룰
# top 을 한칸 아래로 이동
data = stack[top]
stack[top] = None 
top -= 1 
print('bottom =>', stack, '=> top')



