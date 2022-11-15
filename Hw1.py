from fractions import Fraction as fr

def egypt_divide(p:int,q:int)->int:

    if p<1 or p>1000 or q<=p or q>2000:
        print("p와 q의 범위를 재확인하시오")
        return 'error'

    input=fr(p,q)
    res=input
    count=0
    while(res!=0):
        res=res-rev(res)
        count+=1

    return count

def rev(a:fr)->fr:
    tmp =a.denominator//a.numerator
    check=a.denominator%a.numerator
    if check==0:
        return fr(1,tmp)
    else:
        return fr(1,tmp+1)



print("p와q값을 입력하십시오")
p,q=map(int,input().split(" "))
print(egypt_divide(p,q))


