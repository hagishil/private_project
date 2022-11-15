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



print(argmin_2d(b,-3))






