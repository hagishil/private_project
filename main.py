import collections
from collections import deque
from itertools import combinations
import math

def add_Ldecimal(a:str,b:str): # 21자리수 이상  계산
    a = list(a)
    b = list(b)
    if(len(a)> len(b)):
        b=['0' for _ in range(0,len(a)-len(b))]+b
    elif(len(a)<len(b)):
        a=['0' for _ in range(0,len(b) - len(a))]+a
    tmp=[add_upper(x,y) for x,y in zip(a,b)]
    answer=tmp[::-1]
    uten_index = [x for x in range(len(answer)) if int(answer[x]) >= 10]
    while len(uten_index)!=0:
        for x in uten_index:
            answer[x] = answer[x][1]
            if x==len(answer)-1:
                answer.append('1')
            else:
                answer[x+1]=add_upper(answer[x+1],'1')
        uten_index = [x for x in range(len(answer)) if int(answer[x]) >= 10]


    return "".join(answer[::-1])

def add_upper(a:str,b:str)->str:
    answer:int=int(a)+int(b)
    return str(answer)

def max_in_minset(a:list)->int: ###10번
    k=list(set(a))
    k.sort()
    if len(k)%2==1:
        a.pop(0)
    tmp=[min(k[2*x],k[2*x+1])for x in range(len(k)//2)]

    return sum(tmp)
    """
    ## 파이썬 다운 풀이 (단 이경우 입력이 짝수일때라 가정)
    return sum(sorted(a)[::2])
    """
def product_except_self(a: list, i: int) -> list:  # i를 제외한 나머지수 조합으로 가능 곱셈 결과
    a = a[0:a.index(i)] + a[a.index(i) + 1:len(a)]  # a.remove 시간복잡도 n이므로 사용안햇음
    answer = [math.prod(x) for n in range(2, len(a) + 1) for x in list(combinations(a, n))]
    print(answer)
    return answer

def product_except_self_2(a:list)->list:## 11번-2풀이
    result=[]
    p=1
    for i in range(0,len(a)):
        result.append(p)
        p*=a[i]
    p=1
    for i in  range(len(a)-1,-1,-1):
        result[i]*=p
        p*=a[i]
    print(result)
    return result

#######################

def palindrome(a:str)->bool: #알고리즘 인터뷰 1
    a:str=a.lower()
    a:str=a.replace(" ","")
    tmp=[i for i in a if i.isalpha()]
    return tmp==[x for x in tmp[::-1]]


def reverse_string(a:list)->None: #알고리즘 인터뷰 2
    a.reverse()

def reorder_log(a:list)->list: #알고리즘 인터뷰3
    tmp=[i.split(" ") for i in a]
    alpha=[]
    num=[]
    for i in tmp:
        if i[1].isalpha():
            alpha.append(' '.join(i))
        else:
            num.append(' '.join(i))

    alpha.sort(key=lambda x:(x.split(" ")[1:],x.split(" ")[0]))
    return alpha+num

import re
from collections import Counter

def most_common(a:str,b:list[str])->str: #알고리즘 인터뷰 4
    words=[word for word in re.sub('[^\w]',' ',a).lower().split() if word not in b]
    return Counter(words).most_common()[0][0]


def group_anagram(a:list[str])->list: #알고리즘 인터뷰 5
    #tmp=[''.join(sorted(i)) for i in a ]

    r=collections.defaultdict(list)
    for i in a:
        r[''.join(sorted(i))].append(i)
    return r


def longest_palindrome(a:str)->str: #알고리즘 인터뷰 6

    def expand(left:int,right:int)->str:
        while left>=0 and right<len(a) and a[left]==a[right]:
            left-=1
            right+=1
        return a[left+1:right]

    if len(a)<2 or a==a[::-1]: ## 팰린드롬불가하거나 단어전체가 팰린드롬인경우
        #빠른 함수 종료를 위한 일종의 최적화 작업(예외처리 느낌)
        return a

    result=''
    for i in range(len(a)-1):
        result=max(result,expand(i,i+1),expand(i,i+2),key=len)
    return result


def one_trade_max(a:list)->int:
    result=0
    for i in range(0,len(a)-1):
        profit=max(a[i+1:])-a[i]
        if profit>=result:
            result=profit

    print(result)
    return result



def Traipping_rain(a:list)->int:
    stack=[]
    volume=0
    for x in range(len(a)):
        print(stack)
        while stack and a[x]> a[stack[-1]]:
            top=stack.pop()
            if not len(stack): ##len(stack)==0 /0 =false
                break
            distance=x-stack[-1]-1
            waters=min(a[x],a[stack[-1]])-a[top]
            volume+=distance*waters
        stack.append(x)
    print(volume)
    return volume


###알고리즘 인터뷰 3장 연결리스트


class list_node(object):
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

def palidrome_linked_list(head:[list_node])->bool: #알고리즘 인터뷰 13번-runner기법 활용
    ##핵심: 조건문=> 0이외에 숫자: true // 0: false/None 의미
    #핵심2: fast는 2칸 slow는 1칸 && 홀수개 짝수개 전략 구분
    #핵심3: 다중할당
    rev=None
    slow=fast=head

    while fast and fast.next:
        fast=fast.next.next
        rev,rev.next,slow=slow,rev,slow.next
        """
        ##다중할당 개념 숙지
        rev,rev.next=slow,rev
        rev.next,slow=rev,slow.next
        왜 안될까? => rev가 slow를 참조하게 되므로 rev.next가 slow.next를 참조하게 됨
        
        """
        ## 파이썬 참조가 c++과 다른점: 불변,가변객체가 존재, 사용자정의 객체는 가변객체

    if fast:
        slow=slow.next

    while rev and rev.val== slow.val:
        slow,rev=slow.next,rev.next

    return not rev

d=list_node(1)
c=list_node(2,d)
b=list_node(2,c)
a=list_node(1,b)

def merge_sorted_list(a:[list_node],b:[list_node]):
    pass


