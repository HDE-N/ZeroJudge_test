import random as r

a=[]
for ssh in range(2000):
    a.append([])
    for i in range(2000):
        a[ssh].append(r.randint(1,1000000))

with open('j098_09.in','w',encoding='utf-8') as gg:
    for i in a:
        for k in i:
            gg.write(str(k)+' ')
        gg.write('\n')

with open('j098_09.out','w',encoding='utf-8') as gg:
    for ssh in a:
        dp=[ssh[0],max(ssh[0],ssh[1])]
        for i in range(2,len(ssh)):
            dp.append(max(dp[i-1],dp[i-2]+ssh[i]))
        gg.write(str(dp[-1])+'\n')