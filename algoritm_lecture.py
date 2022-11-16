def bubble_sort(a:list)->list: ## python은 call-by object reference
    for x in range(len(a)-1,0,-1):
        for y in range(x):
            if(a[y]>a[y+1]):
                a[y],a[y+1]=a[y+1],a[y]


def insertion_sort(a:list)->list: #삽입 정렬
    result=[]
    for x in a:
        result.append(x)
        if(len(result)<=1):
            pass
        else:
            for y in range(len(result)-1,0,-1):
                if(result[y]<result[y-1]):
                    result[y],result[y-1]=result[y-1],result[y]
                else:
                    pass

    return result

def merge(a:list,b:list)->list: # 병합 정렬 합치기
    if(len(a)==0):
        return b
    elif(len(b)==0):
        return a
    elif(a[0]<=b[0]):
        return a[0:1]+merge(a[1:],b)
    elif(a[0]>b[0]):
        return b[0:1]+merge(b[1:],a)

def merge_sort(a:list)->list: #병합 정렬
    if len(a)==1:
        return a
    return merge(merge_sort(a[:len(a)//2]),merge_sort(a[len(a)//2:]))


def quick_sort(a:list)->list:# 퀵정렬
    pass


def argmin_2d(a: list, axis: int = -3) -> int:
    a_1 = a[0]
    a_2 = a[1]
    result = []

    if axis==-3:
        tmp=[]
        tmp=a_1+a_2
        for i in range(0,len(tmp)):
            if(tmp[i]==sorted(tmp)[0]):
                result.append(i)

    elif axis == 0 or -1:
        for i in range(0, len(a_1)):
            if (a_1[i] < a_2[i]):
                result.append(0)
            else:
                result.append(1)
    elif axis == 1 or -2:

        for i in range(0,len(a_1)):
            if(a_1[i]==sorted(a_1)[0]):
                result.append(i)
        for i in range(0, len(a_2)):
            if (a_2[i] == sorted(a_2)[0]):
                result.append(i)




    return result

def KMP_table(pattern):
    lp = len(pattern)
    tb = [0 for _ in range(lp)]  # 정보 저장용 테이블

    pidx = 0  # 테이블의 값을 불러오고, 패턴의 인덱스에 접근
    for idx in range(1, lp):  # 테이블에 값 저장하기 위해 활용하는 인덱스
        # pidx가 0이 되거나, idx와 pidx의 pattern 접근 값이 같아질때까지 진행
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx - 1]

        # 값이 일치하는 경우, pidx 1 증가시키고 그 값을 tb에 저장
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            tb[idx] = pidx

    return tb

print(KMP_table("aabab"))


print(argmin_2d(b,-3))






