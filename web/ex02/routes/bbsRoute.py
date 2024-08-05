from flask import Blueprint, request
from dao import bbsDAO
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('/')
def bbs_List():
    args = request.args
    print(args.get('page'), args.get('size'))
    rows = bbsDAO.bbs_List(args)
    row = bbsDAO.bbs_Total()
    return {'bbs_Total' : row.get('bbs_Total'), 'bbs_List':rows}

@bp.route('/', methods = ['POST'])
def bbs_Insert():
    data = json.loads(request.get_data())
    result = bbsDAO.bbs_Insert(data)
    return result

@bp.route('/<int:bbs_key>', methods=['Delete'])
def bbs_Delete(bbs_key):
    result = bbsDAO.bbs_Delete(bbs_key)
    return result

@bp.route('/<int:bbs_key>')
def bbs_Read(bbs_key):
    result = bbsDAO.bbs_Read(bbs_key)
    return result

@bp.route('/', methods = ['PUT'])
def bbs_Update():
    data = json.loads(request.get_data())
    result = bbsDAO.bbs_Update(data)
    return result