import json
from io import *
import random
import string
import hashlib

def randstr(n): # 生成长度为 n 的随机字符串，为登录验证做准备
    all_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(all_characters) for _ in range(n))

def encrypt(content: str) -> str:
    """
    简化版MD5加密函数 仅支持字符串输入 返回32位16进制字符串
    """
    # 将字符串转为UTF-8编码的字节串，计算MD5并返回16进制结果
    return hashlib.md5(content.encode('utf-8')).hexdigest()

class s: # 数据库函数
    def __init__(self,name):
        self.name = name
        self.reread()
    def reread(self):
        op = open("./data/"+self.name+".json",'r',encoding="utf-8")
        self.text = op.read()
        op.close()
        self.value = json.loads(self.text)
    def change(self,value):
        self.value = value
        self.text = json.dumps(value)
    def add(self,a,b):
        self.value[a] = b
        self.text = json.dumps(self.value)
    def upd(self): # 此功能感觉多此一举，不应该使用
        print("1")
        self.text = json.dumps(self.value)
    def update(self):
        self.text = json.dumps(self.value)
        op = open("./data/"+self.name+".json",'w',encoding="utf-8")
        op.write(self.text)
        op.close()

if __name__=="__main__":
    pass