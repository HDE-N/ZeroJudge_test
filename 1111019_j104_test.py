import random as r

a=[]
for ssh in range(20):
    a.append([])
    for i in range(100000):
        a[ssh].append(r.randint(1,100000000))

with open('j104_08.in','w',encoding='utf-8') as gg:
    for i in a:
        for k in i:
            gg.write(str(k)+' ')
        gg.write('\n')

with open('j104_08.out','w',encoding='utf-8') as gg:
    for ssh in a:
        dp=[ssh[0]]
        s=0
        for i in range(1,len(ssh)):
            if s<ssh[i]-dp[i-1]:s=ssh[i]-dp[i-1]
            if dp[i-1]>ssh[i]:dp.append(ssh[i])
            else:dp.append(dp[i-1])
        gg.write(str(s)+'\n')