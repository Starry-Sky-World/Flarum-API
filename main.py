from flask import Flask, request, jsonify, render_template
import requests
from flask_cors import CORS
import json
import random
import os
import logging
import colorlog
"""
GNU AGPLv3
"""
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    "{asctime} {log_color}[{levelname}] - {message}",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
    style='{'
))

# 创建Logger对象并添加handler
logger = colorlog.getLogger()
logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app,resources=r'/*')

AdminName = os.getenv("FlarumAdminName")
AdminPassword = os.getenv("FlarumAdminPassword")
FlarumLink = os.getenv("FlarumLink")
logging.warning("请勿打开CDN/WAF的JS防护！")
logging.error(f"链接：{FlarumLink}")

@app.route('/', methods=['GET','POST'])
def index():
    # 这里定义你想要返回的数据
    return {
        "status":"200",
        "server":"Run"
    }

@app.route('/api/token', methods=['GET'])
def Get_Token():
    UserName = request.args.get("username")
    UserPassword = request.args.get("password")
    Rdata_a = {
        "identification":UserName,
        "password":UserPassword
    }
    return requests.post(f"{FlarumLink}/api/token",json=Rdata_a).json
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8050)