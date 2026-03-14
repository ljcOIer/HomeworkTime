# 造数据机器
import data_tool as o
from app.database import SUBJECT
import name_tool
from random import randint,random,choice

user = o.s("user")
SchoolList = o.s("SchoolList")
classwork = o.s("classWork")

sc = "广州市第七中学"

def solve_user(): # 生成6个年级16个班，45个人的数据。
    user.value[sc] = {"teacher":{},"principal":{},"student":{}}
    SchoolList.value[sc] = {}
    for i in SUBJECT: # teacher
        user.value[sc]["teacher"]["{}_teacher".format(i)] = {
            "name" : "{}老师".format(SUBJECT[i]),
            "password" : o.randstr(10),
            "subject" : [i],
            "class" : [["1","1"],["1","2"],["1","3"],["2","1"],["2","2"],["2","3"]]
        }
    user.value[sc]["principal"]["admin"] = {
        "name":"admin",
        "password": "admin123",
        "subject" : list(SUBJECT),
        "class"   : [["1",str(i)] for i in range(1,17)]
    }
    for i in range(1,7):
        SchoolList.value[sc][str(i)] = {}
        for j in range(1,randint(13,17)):
            SchoolList.value[sc][str(i)][str(j)] = []
            for k in range(1,randint(40,50)):
                user.value[sc]["student"]["{}0{}0{}".format(i,j,k)] = {
                    "name" : name_tool.randnamestr(),
                    "password":o.randstr(5),
                    "subject":[round(random(),3),round(random(),3)],
                    "read_speed":randint(1,100),
                    "class":[str(i),str(j)]
                }
                SchoolList.value[sc][str(i)][str(j)].append("{}0{}0{}".format(i,j,k))

homework_text = ["抄写书本","背书","一张卷子","练习册","改卷","整理错题","抄写书本一百遍","读书"]
task_id_list = ["第2周周末","第3周周末","第4周周末","清明节假期","第6周周末","第7周周末","第8周周末","第9周周末"]

def solve_classwork():
    classwork.value[sc] = {}
    for task in task_id_list:
        classwork.value[sc][task] = {}
        for i in SchoolList.value[sc]:
            classwork.value[sc][task][i] = {}
            for j in SchoolList.value[sc][i]:
                classwork.value[sc][task][i][j] = {}
                for sub in SUBJECT:
                    num = randint(1,5)
                    classwork.value[sc][task][i][j][sub] = {
                        "information":[{"text":choice(homework_text),"word_count":randint(1,10000),"hard":round(random(),3)} for kk in range(num)],
                        "time_average":[randint(50,200) for kk in range(num)]+[randint(num*50,num*200)],
                        "time":{
                            kk:[randint(50,200) for kkk in range(num)] for kk in SchoolList.value[sc][i][j]
                        }
                    }

if __name__ == "__main__":
    # print(o.randstr(10))
    # solve_user()
    # user.update()
    # SchoolList.update()
    solve_classwork()
    classwork.update()
    # print(classwork.value)
