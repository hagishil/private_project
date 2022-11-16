from collections import deque

def rome_num(a:str)->int:
    a=deque(a.lower())
    stack=deque()
    num_is={"i":1,"x":10,"v":5}
    result=0

    for i in a:
        if i=="i":
            if len(stack)==2: #x,v와 조합하여 최대 연속할수있는 i의 갯수
                result=result+num_is[stack.pop()]
            stack.append(i)
        else:
            result=result+num_is[i]-len(stack)
            stack.clear()

    return result

# a="xiiix" //이경우 어떻게 할것인가?

print("로마숫자를 입력하시오")
a=input()

print(rome_num(a))










