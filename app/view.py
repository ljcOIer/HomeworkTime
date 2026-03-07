# view.py
from flask import Blueprint, render_template_string, render_template, request, redirect, session, Response, jsonify
from flask_cors import CORS
# from app.database import *

app = Blueprint('view', __name__, url_prefix="")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/basic')
def basic():
    return render_template('basic.html')

@app.route('/login')
def login():
    school_list = [
        "广州市第七中学",
        "广州市第一中学",
        "广州市第二中学"
    ]
    
    # 2. 设置默认选中的学校（可选，根据业务需求调整）
    default_selected_school = "广州市第七中学"
    return render_template('Login.html', SchoolList=school_list, default_school=default_selected_school)