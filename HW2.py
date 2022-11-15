
def hurdle_stairs(n:int,a:int,b:int)->int:
    if a==n or b==n:
        return 0

    tmp=[0]
    while True:
        tmp_2=[]
        check=0
        for i in tmp:
            if(i==n):
                tmp_2.append(i)
            if(i+1 !=a and i+1 !=b and i+1<=n):
                tmp_2.append(i+1)
                check+=1
            if(i+2 !=a and i+2 !=b and i+2<=n):
                tmp_2.append(i+2)
                check+=1
        if(check==0):
            break
        tmp=tmp_2

    if(tmp[0]==0 and len(tmp)==1):
        return 0

    return len(tmp)





print("n,a,b값을 입력하시오")
a,b,c=map(int,input().split(' '))
print(hurdle_stairs(a,b,c))
