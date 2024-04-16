### 함수 ###
def addNumber(num) :
    if  num == 1 :
        return 1
    return num + addNumber(num-1)

### 변수 ###
print(addNumber(10))

# 반복문이 없는데도 반복문의 효과를 낸다 
