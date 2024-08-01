from dao import db

def list(bbs_key, args):
    page = int(args['page'])
    size = int(args['size'])
    start = (page-1) * size 
    try:
        with db.connection.cursor() as cursor:
            sql = "select *, date_format(reply_regDate, '%%Y-%%m-%%d %%T') as fmtdate from reply where bbs_key=%s order by reply_key desc limit %s, %s"
            cursor.execute(sql, (bbs_key, start, size))
            rows = cursor.fetchall()
            return rows
    except Exception as err:
        print('목록오류', err)
    finally:
        cursor.close()

def insert(reply):
    try:
        with db.connection.cursor() as cursor:
            sql = "insert into reply(bbs_key, reply_contents, reply_writer) values (%s, %s, %s)"
            cursor.execute(sql, (reply.get("bbs_key"), reply.get("reply_contents"), reply.get("uid")))
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('댓글 등록 오류 ', err)
        return 'fail'
    finally :
        cursor.close()

def total(bbs_key):
    try:
        with db.connection.cursor() as cursor:
            sql = "select count(*) reply_total from reply where bbs_key=%s"
            cursor.execute(sql, bbs_key)
            row = cursor.fetchone()
            return row
    except Exception as err:
        print('댓글 개수 오류', err)
    finally:
        cursor.close()

def delete(reply_key):
    try:
        with db.connection.cursor() as cursor:
            sql = "delete from reply where reply_key=%s"
            cursor.execute(sql, reply_key)
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('댓글 삭제 오류 ', err)
        return 'fail'
    finally :
        cursor.close()

def update(reply):
    try:
        with db.connection.cursor() as cursor:
            sql = "update reply set reply_contents=%s, reply_regDate=now() where reply_key=%s"
            cursor.execute(sql, (reply.get('reply_contents'), reply.get('reply_key')))
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('댓글 수정 오류 ', err)
        return 'fail'
    finally :
        cursor.close()