import random as r

s=[]
with open('j228_09.in','w',encoding='utf-8') as tk:
    for i in range(5):         # i 筆資料
        s.append([])
        for k in range(1000000):     # k 個數字
            g=r.randint(-1000000,1000000)   #範圍
            tk.write(str(g)+' ')
            s[i].append(g)
        tk.write('\n')


with open('j228_09.out','w',encoding='utf-8') as tk:
    for a in s:
        for i in range(1,len(a)):
            if a[i-1]>0:a[i]+=a[i-1]
        tk.write(str(max(a))+'\n')