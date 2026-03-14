# backupDATA.py - 保存json数据
import os
import sys
import datetime

def get_datetime():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d-%H-%M-%S')
    return formatted_time

def update():
    datadir="./data/"
    nowdir = "./copy_data/{}".format(get_datetime())
    print("add dir:",nowdir)
    os.makedirs(nowdir)

    for item in os.listdir(datadir):
        # 拼接完整路径
        item_path = os.path.join(datadir, item)
        new_path = os.path.join(nowdir, item)
        # 筛选仅文件（排除子文件夹）
        if os.path.isfile(item_path):
            print(item_path)
            o = open(item_path,"r",encoding="utf8")
            datastr = o.read()
            o.close()
            o = open(new_path,"w",encoding="utf8")
            o.write(datastr)
            o.close()

if __name__=="__main__":
    update()