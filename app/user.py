# user.py
from flask import Blueprint, render_template_string, render_template, request, redirect, session, Response, jsonify
from flask_cors import CORS
from app.database import *

app = Blueprint('user', __name__, url_prefix="/user")

@app.route('/login', methods=['POST'])
def login():
    # 1. 设置默认值，避免 None
    username = request.form.get('username', '')  # 无值时返回空字符串
    password = request.form.get('password', '')
    identity = request.form.get('identity', '')  # 无值时返回空字符串
    school = request.form.get('school', '')
    # 2. 推荐返回 JSON 格式（前端更容易解析，Content-Type: application/json）
    response_data = {
        "username": username,
        "password": password,  # 实际项目中不要返回密码，仅演示
        "identity": identity,
        "school": school,
        "status": "success"
    }
    return jsonify(response_data)