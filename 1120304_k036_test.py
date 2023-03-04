import random as r

s1='k036_09.in'
s2='k036_09.out'

sp=[]
with open(s1,'w',encoding='utf-8') as k:
    for ssh in range(1):       #List數量
        nums=[]
        for i in range(4200):     #List長度
            nums.append(r.randint(0,9))
        for i in nums:k.write(str(i)+' ')
        k.write('\n')
        while len(nums)>1:
            s=[]
            for i in range(len(nums)-1):
                s.append((nums[i]+nums[i+1])%10)
            nums=[x for x in s]            
        sp.append(nums[0])

with open(s2,'w',encoding='utf-8') as k:
    for i in sp:
        k.write(str(i)+'\n')