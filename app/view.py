# view.py
from flask import Blueprint, render_template_string, render_template, request, redirect, session, Response, jsonify
from flask_cors import CORS
from app.database import *

app = Blueprint('view', __name__, url_prefix="")

@app.route('/')
def index():
    if verify_cookies(request.cookies):
        return redirect('/tasklist')
    return render_template('index.html')

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/login')
def login():
    if verify_cookies(request.cookies):
        return redirect('/tasklist')
    school_list = SchoolListDATA.value
    identity_param = request.args.get('identity')
    default_selected_school = "广州市第七中学"
    return render_template('Login.html', SchoolList=school_list, default_school=default_selected_school,identity=identity_param,error="")

@app.route('/tasklist')
def tasklist():
    if not verify_cookies(request.cookies):
        return redirect('/')
    return render_template('TaskList.html')

@app.route('/task/<task_id>')
def task_detail(task_id):
    if not verify_cookies(request.cookies):
        return redirect('/')
    return render_template('TaskInformation.html', task_id=task_id)