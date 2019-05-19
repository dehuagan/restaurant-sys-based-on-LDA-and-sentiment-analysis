# -*- coding: utf-8 -*-
from flask_cors import *
from flask import Flask
#到虚拟环境下pip install
from flask_sqlalchemy import SQLAlchemy


#创建项目对象

app = Flask(__name__)
app.config.from_object('panew.setting')
CORS(app, supports_credentials=True)
#创建数据库对象
db = SQLAlchemy(app)