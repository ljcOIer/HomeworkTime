# main.py
HOST = "0.0.0.0"
Debug = True
PORT = 5000
static_url_path = ''
static_folder   = 'static'
template_folder = 'templates'

from flask import Flask
from app import user,view
from flask_cors import CORS

def create_app():
    app = Flask(__name__,
            static_url_path=static_url_path,
            static_folder=static_folder,
            template_folder=template_folder)

    CORS(app, resources={r"/*": {"origins": "*"}})
    # 注册蓝图
    app.register_blueprint(user.app)
    app.register_blueprint(view.app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=Debug, host=HOST, port=PORT)