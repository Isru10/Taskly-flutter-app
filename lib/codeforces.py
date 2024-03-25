'''#ugr/25476/14
#Lab3
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    for j in range(len(arr)):
        if arr[j]<0:
            arr[j]=arr[j]*-1
    print(sum(arr))
             '''
'''arr=[]
for i in range(len(s)):
    arr.append(s[i])
arr2=[]
while len(arr)>2:
        if len(arr)%2==0:
            arr2.append(arr[(len(arr)//2)-1])
            arr.remove(s[arr[(len(arr)//2)-1]])
        else:
             arr2.append(arr[(len(arr)//2)])
             arr.remove(arr[(len(arr)//2)])
for i in range(len(arr)):
     arr2.append(arr[i])
print(''.join(arr2))
'''
#ugr/25476/14
#lab3
k1, k2, k3 = map(int, input().split())
 
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())
 
a = sorted(a)
b = sorted(b)
c = sorted(c)
 
n = k1 + k2 + k3
 
l = [0] * (n + 1)
r = [0] * (n + 1)
 
p = 0
for i in range(n + 1):
	if p < len(a) and i == a[p]:
		p += 1
	l[i] += len(a) - p
 
p = 0
for i in range(n + 1):
	if p < len(b) and i == b[p]:
		p += 1
	l[i] += p
 
p = 0
for i in range(n + 1):
	if p < len(b) and i == b[p]:
		p += 1
	r[i] += len(b) - p
 
p = 0
for i in range(n + 1):
	if p < len(c) and i == c[p]:
		p += 1
	r[i] += p
 
r_cum_min = [None] * (n + 1)
r_cum_min[-1] = r[n]
 
i = n - 1
while i >= 0:
	r_cum_min[i] = min(r[i], r_cum_min[i + 1])
	i -= 1
 
answer = 1e9
for i in range(n + 1):
	if l[i] + r_cum_min[i] < answer:
		answer = l[i] + r_cum_min[i]

 
print(answer)