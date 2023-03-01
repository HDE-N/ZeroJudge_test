import random as r
import copy

t=1500
sp=r.randint(20,150)
ms=r.randint(150,250)
n=6000
ss=[]
with open('j962_09.in','w',encoding='utf-8') as k:
    k.write('%d,%d,%d\n%d\n'%(t,sp,ms,n))
    for i in range(n):
        g=r.randint(1,10)
        if g==1:
            sk='q'
        elif 2<=g<=3:sk='n'
        elif 4<=g<=5:sk='e'
        elif 6<=g<=7:sk='~b'
        else:sk='b'
        ss.append(sk)
        k.write(sk+'\n')

'''
def s1():       #人律
    global t,sp,ms,atk,combo,dou
    a=input()
    if a=='b':      #普攻
        if t>=0.9:
            combo+=1
            atk+=10
            sp+=2
            if combo==4:
                combo=0
                atk+=10
                sp+=5
        t-=0.9
    elif a=='~b':   #蓄力
        if t>=1.5:
            combo=0
            if dou==1:
                dou-=1
                atk+=20
            atk+=20
            sp+=10
        t-=1.5
    elif a=='e':    #武器技
        if t>=1:
            combo=0
            atk+=12
        t-=1
    elif a=='n':    #極限閃避
        combo=0
        t+=3
        sp+=12
        dou+=1
        if dou>1:dou-=1
    else:           #必殺技
        combo=0
        if sp<125:t-=0.5
        else:
            global p,c1,c2
            sp-=125
            p=2
            c1=2
            c2=1
            atk+=20

def s2():       #始源律
    global t,sp,ms,atk,combo,tp
    if tp>=20:
        global p
        atk+=30
        p=1
        return 0
    a=input()
    if a=='b':
        if t>=0.8:
            combo+=1
            atk+=20
            if combo==4:
                combo=0
                atk+=30
                sp+=5
        t-=0.8
        tp+=0.8
    elif a=='~b':
        if t>=2:
            combo=0
            atk+=40
            sp+=10
        t-=2
        tp+=2
        if t>=2.2:
            atk+=50
            sp+=5
        t-=2.2
        tp+=2.2
    elif a=='e':
        global c1
        combo=0
        if c1>0:
            if t>=2.2:
                c1-=1
                atk+=50
                sp+=5
            t-=2.2
            tp+=2.2
        else:
            t-=0.5
            tp+=0.5
    else:
        combo=0
        global c2
        if c2>0:
            c2-=1
            t+=5
            tp-5
            atk+=50
            sp+=5
        else:
            t-=0.5
            tp+=0.5


p=1         #型態控制
atk=0       #累積傷害
combo=0     #普攻連擊
dou=0       #蓄力雙倍(人律)
c1,c2=0,0   #武器技&極限閃避使用次數(始源律)
tp=0        #往世星海持續時間
for ssh in ss:
    if t>0:
        if p==1:
            s1(ssh)
        else:
            s2(ssh)
    else:break
    if sp>ms:
        sp=copy.copy(ms)
print(atk)
'''