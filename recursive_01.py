# 재귀함수

### 함수 ###
def open_box():
    global count
    print('open the box. . . ')
    count -= 1 
    if count == 0 :
        print('this is the present for y o u ! !')
        return # 전으로  계속 리턴 리턴 리턴 

    open_box() # 무한 루프에 빠진다  -> 종료 제시 
    print('close the box . . . ') # 종료조건을 만났을때 이후 실행 되는 코드 
 

    



### 메인 ###
count = 3
open_box() 
