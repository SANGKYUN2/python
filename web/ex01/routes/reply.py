from flask import Blueprint, request
from dao import reply
import json

bp = Blueprint('reply', __name__, url_prefix='/reply')

@bp.route("/list.json/<int:bbs_key>")
def list(bbs_key):
    args = request.args
    rows = reply.list(bbs_key, args)
    row = reply.total(bbs_key)
    data = {'total':row.get('reply_total'), 'list':rows}
    return data

@bp.route("/insert", methods = ["POST"])
def insert() :
    req = json.loads(request.get_data())
    result = reply.insert(req)
    return result

@bp.route("/<int:reply_key>", methods = ["DELETE"])
def delete(reply_key):
    result = reply.delete(reply_key)
    return result

@bp.route("/update", methods=['POST'])
def update() :
    req = json.loads(request.get_data())
    result = reply.update(req)
    return result
