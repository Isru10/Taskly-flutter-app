"""from collections import *
t=int(input())
for i in range(t):
    s=set()
    n=int(input())
    m=list(map(int,input().split()))
    cnt=Counter(m)
    ans=0
    for i , num in enumerate(cnt):
        if cnt[num]==1:
            ans=num
    print(m.index(ans)+1)
"""
'''n=int(input())
s=[]
for i in range(n):
    arr=list(map(int,input().split()))
    s.append(sum(arr))
if sum(s)==0:
    print("YES")
else:
    print("NO")
'''
'''n,k=map(int,input().split())
arr=list(map(int,input().split()))
l=0
mxlen=0
s=k
win=0
for r in range(n):
    win+=arr[r]
    if win>s:
        win-=arr[l]
        l+=1
    mxlen=max(mxlen,r-l+1)
print(mxlen)'''
'''n=int(input())
f=[]
s=[]
t=[]
for i in range(n):
    arr=list(map(int,input().split()))
    f.append(arr[0])
    s.append(arr[1])
    t.append(arr[2])
if sum(f)==0 and sum(s)==0 and sum(t)==0:
    print("YES")
else:
    print("NO")'''
'''r=input()
add=[]
for i in range(len(r)):
    if len(add)==0:
        add.append(r[i])
    elif add[len(add)-1]==r[i]:
        add.pop()
    else:        
        add.append(r[i])
if len(add)==0:
    print("Yes")
else:
    print("No")'''
'''t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    cnt=0
    m={}
    for i in range(n):
        if s[i] in m:
            m[s[i]]+=1
        else:
            m[s[i]]=1
    for key in m:
        if m[key]&1:
            cnt+=1
    cnt-=1
    if k<cnt:
        print("NO")
    else:
        print("YES")
        '''
'''n=int(input())
arr=list(map(int,input().split()))
sol=[]
for i in range(len(arr)-1):
    idx=i 
    m=arr[i]
    for j in range(i+1,len(arr)):
        if arr[j]<m:
            idx=j
            m=arr[j]
    if not idx==i:
        arr[i],arr[idx]=arr[idx],arr[i]
        sol.append([i, idx])
print(len(sol))
for i in sol:
    print(i[0], i[1])
    '''
'''t=int(input())
for _ in range(t):
    cnt=0
    n=int(input())
    sol=[]
    for i in range(n):
        arr=list(map(int,input().split()))
        sol.append(arr)
    sol.sort()
    for p in range(len(sol)-1):
        m=sol[p][1]
        for j in range(p+1,len(sol)):
            if m>sol[j][1]:
                cnt+=1
    print(cnt)'''
'''def m(lt,rt):
    l=0
    r=0
    global ans
    temp=0
    res=[]
    while l<len(lt) and r<len(rt):
        if lt[l]<rt[r]:
            res.append(lt[l])
        else:
            res.append(rt[r])
            r+=1
            temp+=1
    while l<len(lt):
        res.append(lt[l])
        ans+=temp
        l+=1
    while l<len(lt):
        res.append(rt[r])
        r+=1
    return res
def gts(nums):
    if len(nums)<=1:
        return nums 
    mid=len(nums)//2
    ltb=gts(nums[:mid])
    rtb=gts(nums[mid:])
    return m(ltb,rtb)
t=int(input())
for _ in range(t):
    n=int(input())
    pos=[]
    ans=0
    for _ in range(n):
        a,b = list(map(int,input().split()))
        pos.append([a,b])
    pos.sort()
    second=[i[1] for i in pos]
    gts(second)
    print(ans)''''''

t=int(input())
for _ in range(t):
    n=int(input())
    t=0
    d=0
    while True :
        if n%3==0:
            n=n//3
            t+=1
        else:
            break 
    while True :
        if n%2==0:
            n=n//2
            d+=1
        else:
            break 
    if t>=d and n==1:
        print(2*t-d)'''
'''
a,b,c=list(map(int,input().split()))
def gcd(a,b):
    l=max(a,b)
    s=min(a,b)
    r=l%s
    if r==0:
        return s
    else:
        return gcd(s,r)
tot=c
trn=1
while tot>0:
    if trn ==1:
        tot -=gcd(tot,a)
        trn=0
    else:
        tot -=gcd(tot,b)
        trn=1
print(trn)'''
'''t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    cnt=0
    m={}
    for i in range(n):
        if s[i] in m:
            m[s[i]]+=1
        else:
            m[s[i]]=1
    for key in m:
        if m[key]&1:
            cnt+=1 
    cnt-=1
    if k<cnt:
        print("NO")
    else:
        print("YES")'''
'''n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append(x+y)
print(max(arr))'''
'''s=input()
t=input()
cnt=1
for i in range(max(len(s),len(t))):
        ns=s
        nt=t
        if ns in nt:
            cnt+=len(nt)-len(ns)
            break
        else:
            ns=ns[i+1:]
            cnt+=1
print(cnt)'''
'''n=int(input())
s=input()
arr=[]
for i in range(1,n+1):
    if n%i==0:
        arr.append(i)
for i in range(len(arr)):
    nt=s[:arr[i]]
    nt=nt[::-1]
    s=nt+s[arr[i]:]
print(s)
'''

#ugr/25476/14
#Lab 3
str =list(map(int, input().split()))
n,m=str[0],str[1]
arr = list(map(int, input().split()))
ans = arr[0]-1
s =ans
for i in range(m-1):
    ans = arr[i+1]-arr[i]
    if ans<0:
        s += n+ans
    else:s+=ans
print(s)

'''

'''