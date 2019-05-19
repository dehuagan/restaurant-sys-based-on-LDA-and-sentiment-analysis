from flask import jsonify

def response_pretreat(type,code,msg):
    response = jsonify({'type':type,'code':code,'msg':msg})
    return response