# user.py
from flask import Blueprint, render_template_string, render_template, request, redirect, session, Response, jsonify
from flask_cors import CORS
from app.database import *
import data_tool

app = Blueprint('user', __name__, url_prefix="/user")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    identity = request.form.get('identity')
    school = request.form.get('school')
    # return user.value
    if not username or not password:
        return render_template("login.html", error="请输入用户名和密码", SchoolList=SchoolListDATA.value, default_school=school, identity=identity) 
    if school not in user.value:
        return render_template("login.html", error="不存在中学", SchoolList=SchoolListDATA.value, default_school=school, identity=identity) 
    if identity not in user.value[school]:
        return render_template("login.html", error="身份信息不正确", SchoolList=SchoolListDATA.value, default_school=school, identity=identity) 
    if username not in user.value[school][identity]:
        return render_template("login.html", error="用户名不存在", SchoolList=SchoolListDATA.value, default_school=school, identity=identity)
    if user.value[school][identity][username]['password'] != password:
        return render_template("login.html", error="密码错误", SchoolList=SchoolListDATA.value, default_school=school, identity=identity)
    ret = redirect('/tasklist')
    ret.set_cookie('username',username)
    ret.set_cookie('school',school)
    ret.set_cookie('identity',identity)
    ret.set_cookie('pass_str',data_tool.encrypt(password))
    return ret

@app.route('/logout')
def logout():
    ret = redirect('/')
    ret.delete_cookie('username')
    ret.delete_cookie('school')
    ret.delete_cookie('identity')
    ret.delete_cookie('pass_str')
    return ret