# admin.py - 管理页面处理
from flask import Blueprint, render_template_string, render_template, request, redirect, session, Response, jsonify
from flask_cors import CORS
from app.database import *
import data_tool

gradeTOstr = {"1":"初一","2":"初二","3":"初三","4":"高一","5":"高二","6":"高三"}

app = Blueprint('admin', __name__, url_prefix="/admin")

@app.route('/')
def index():
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    return render_template('AdminIndex.html',user_identity=id)

@app.route('/tasks')
def tasklist():
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    task_list = [[kk,"是"] for kk in classwork.value[sc]]
    return render_template('AdminTasklist.html',user_identity=id, task_list=task_list)

@app.route('/task/<task_id>/subject/<sub>')
def task_detail_subject(task_id,sub):
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    task_list = []
    for i in classwork.value[sc][task_id]:
        for j in classwork.value[sc][task_id][i]:
            task_list.append([i,j,
                "<br>".join([ kk["text"] \
                 for kk in classwork.value[sc][task_id][i][j][sub]["information"]]),
                            o.time_str(classwork.value[sc][task_id][i][j][sub]["time_average"][-1]),"是",
                            gradeTOstr[i]])
    return render_template('AdminTaskSubject.html', task_id=task_id,user_identity=id,sub=sub, task_list=task_list)

@app.route('/task/<task_id>/subject')
def task_detail_subject_(task_id):
    return redirect("/admin/task/{}/subject/chinese".format(task_id))


@app.route('/task/<task_id>/class/<grade>/<cls>')
def task_detail_class(task_id,grade,cls):
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    task_list = []
    for sub in classwork.value[sc][task_id][grade][cls]:
        task_list.append([sub,
                "<br>".join([ kk["text"] \
                 for kk in classwork.value[sc][task_id][grade][cls][sub]["information"]]),
                            o.time_str(classwork.value[sc][task_id][grade][cls][sub]["time_average"][-1]),"是",
                            SUBJECT[sub]])

    gradelist = [("1","初一"),("2","初二"),("3","初三"),("4","高一"),("5","高二"),("6","高三")]
    classlist = list(SchoolList.value[sc][grade])
    userlist = []
    for i in SchoolList.value[request.cookies.get('school')][grade][cls]:
        userlist.append([i,user.value[sc]["student"][i]["name"],
                         user.value[sc]["student"][i]["subject"][-1],
                         user.value[sc]["student"][i]["password"]])
    return render_template('AdminTaskClass.html', task_id=task_id,user_identity=id,grade=grade,cls=cls, task_list=task_list, 
                           userlist=userlist, gradelist=gradelist, classlist=classlist)

@app.route('/task/<task_id>/class')
def task_detail_class_(task_id):
    return redirect("/admin/task/{}/class/1/1".format(task_id))

@app.route('/task/<task_id>/information/<grade>/<cls>/<sub>')
def task_detail_information(task_id,grade,cls,sub):
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    Sub = SUBJECT[sub]
    xx = classwork.value[sc][task_id][grade][cls][sub]
    task_list = []
    for i in range(len(xx["information"])):
        task_list.append([i+1,xx["information"][i]["text"],o.time_str(xx["time_average"][i],)])
    return render_template('AdminTaskInformation.html', task_id=task_id,user_identity=id,grade=grade,cls=cls,Sub=Sub,sub=sub,
                           averagetime=o.time_str(xx["time_average"][-1]),task_list=task_list)

@app.route('/task/<task_id>/information/<grade>/<cls>/<sub>/studentlist')
def task_detail_information_studentlist(task_id,grade,cls,sub):
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    Sub = SUBJECT[sub]
    xx = classwork.value[sc][task_id][grade][cls][sub]
    yy = xx["time"]
    task_list = []
    for kk in yy:
        print(kk)
        task_list.append([kk,user.value[sc]["student"][kk]["name"]]+[
                          o.time_str(tim) for tim in yy[kk]])
    return render_template('AdminTaskInformationStudent.html', task_id=task_id,user_identity=id,grade=grade,cls=cls,Sub=Sub,sub=sub,
                           task_list=task_list,lenn=len(task_list[0])-3)

@app.route("/user")
def user_():
    return redirect("/admin/user/1/1")

@app.route("/user/<grade>/<cls>")
def user_list(grade,cls):
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    sc = request.cookies.get('school')
    gradelist = [("1","初一"),("2","初二"),("3","初三"),("4","高一"),("5","高二"),("6","高三")]
    classlist = list(SchoolList.value[sc][grade])
    userlist = []
    for i in SchoolList.value[request.cookies.get('school')][grade][cls]:
        userlist.append([i,user.value[sc]["student"][i]["name"],
                         user.value[sc]["student"][i]["subject"][-1],
                         user.value[sc]["student"][i]["password"]])
    return render_template("AdminUser.html",grade=grade,cls=cls, gradelist=gradelist,classlist=classlist,userlist=userlist)

@app.route("/user/setpassword/<x>/<y>", methods=['POST'])
def user_set_password(x,y):
    global user
    if not verify_cookies(request.cookies):
        return redirect('/')
    id = get_identity(request.cookies)
    if not id:
        return redirect('/tasklist')
    user_id = request.form.get('id')
    password = request.form.get('password')
    user.value[request.cookies.get('school')]["student"][user_id]["password"] = password
    return "ok"


