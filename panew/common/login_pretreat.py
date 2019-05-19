# _*_ coding: utf-8 _*_
from panew.model.student_info import student_info
from panew.model.teacher_info import teacher_info
from panew.model.study_style import study_style
from panew.model.emailcode import emailcode
from panew.common.tokenmethod import encryptoken
from panew.model.student_login import student_login
from panew.model.teacher_login import teacher_login
from panew.model.admin import admin

from panew import app
from flask import request,render_template,flash,abort,url_for,redirect,Flask,session
import json
from flask import jsonify
from panew.common.emailvalidation import email_validation
from panew import db
import time
from panew.common.response_pretreat import response_pretreat
from panew.model.teacher_info import teacher_info
from panew.model.student_info import student_info
from panew.model.admin import admin

def login_pretreat(type,data):
    if(type != data['type']):
        code = 0
        msg = '接口型号不吻合'
        return response_pretreat(type,code,msg)

    token_2 = data['token']
    has_teacher_token = teacher_info.query.filter_by(ti_token=token_2).first()
    has_student_token = student_info.query.filter_by(si_token=token_2).first()
    has_admin_token = admin.query.filter_by(admin_token=token_2).first()


    if token_2 == None:
        code = 2
        msg = '没有传入token'
        return response_pretreat(type,code,msg)

    if ((has_teacher_token == None) and (has_student_token==None) and (has_admin_token==None)):
        code = 3
        msg = 'token已过期'
        return response_pretreat(type,code,msg)

    if(has_teacher_token != None):
        if has_teacher_token.ti_id != data['user_id']:
            code = 3
            msg = 'token已过期'
            return response_pretreat(type, code, msg)


    if(has_student_token != None):
        if has_student_token.si_id != data['user_id']:
            code = 3
            msg = 'token已过期'
            return response_pretreat(type, code, msg)

    if(has_admin_token != None):
        if has_admin_token.admin_id != data['user_id']:
            code = 3
            msg = 'token已过期'
            return response_pretreat(type, code, msg)
