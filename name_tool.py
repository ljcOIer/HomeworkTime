# 名字生成器
import random

o = open("name.txt","r",encoding="utf8")
namelist = o.read().split("、")
o.close()

a = {}
b = {}
c = {}

for name in namelist:
    a[name[0]] = 1
    b[name[1]] = 1
    try:
        c[name[2]] = 1
    except:
        pass

def randnamestr():
    return random.choice(list(a))+random.choice(list(b))+random.choice(list(c))
