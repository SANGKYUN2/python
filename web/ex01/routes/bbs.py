from flask import Blueprint, render_template, request
from dao import bbs
import json

bp = Blueprint('bbs', __name__, url_prefix='/bbs')

@bp.route('')
def list():
    return render_template('index.html', title='게시판', pageName='bbs/list.html')

@bp.route('/list.json')
def listJSON():
    args = request.args
    page = args['page']
    size = args['size']
    list = bbs.list(page, size)
    total = bbs.total()
    data = {'total' : total.get('bbs_total'), 'list':list}
    return data

@bp.route('/insert')
def insert():
    return render_template('index.html', title='글쓰기', pageName='bbs/insert.html')

@bp.route('/insert', methods=['POST'])
def insertPost():
    req = json.loads(request.get_data())
    print(req)
    result = bbs.insert(req)
    return result

@bp.route('/<int:bbs_key>')
def read(bbs_key):
    vo=bbs.read(bbs_key)
    return render_template('index.html', bbs=vo, title='게시글 정보', pageName='bbs/read.html')

@bp.route('/<int:bbs_key>', methods=['DELETE'])
def delete(bbs_key):
    result = bbs.delete(bbs_key)
    return result

@bp.route('/update/<int:bbs_key>')
def update(bbs_key):
    vo = bbs.read(bbs_key)
    return render_template('index.html', bbs=vo, title="게시글 수정", pageName='bbs/update.html')

@bp.route('update', methods=['POST'])
def updatePost():
    req = json.loads(request.get_data())
    result = bbs.update(req)
    return result
