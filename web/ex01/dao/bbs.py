from dao import db

def list(page, size):
    page = int(page)
    size = int(size)
    start = (page-1) * size
    try:
        with db.connection.cursor() as cursor:
            sql = "select *, date_format(bbs_regDate, '%%Y-%%m-%%d %%T') as fmtdate from bbs order by bbs_key desc limit %s, %s"
            cursor.execute(sql, (start, size))
            rows = cursor.fetchall()
            return rows
    except Exception as err:
        print('목록오류 : ', err)
    finally:
        cursor.close()

def insert(bbs):
    try :
        with db.connection.cursor() as cursor:
            sql = "insert into bbs(bbs_title, bbs_writer, bbs_contents) values (%s, %s, %s)"
            cursor.execute(sql, (bbs.get('bbs_title'), bbs.get('uid'), bbs.get('bbs_contents')))
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('등록오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def read(bbs_key):
    try :
        with db.connection.cursor() as cursor:
            sql = "select *, date_format(bbs_regDate, '%%Y-%%m-%%d %%T') as fmtdate  from bbs where bbs_key=%s"
            cursor.execute(sql, bbs_key)
            row = cursor.fetchone()
            return row
    except Exception as err:
        print('게시글 읽기 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def delete(bbs_key):
    try :
        with db.connection.cursor() as cursor:
            sql = "delete from bbs where bbs_key=%s"
            cursor.execute(sql, bbs_key)
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('삭제오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def update(bbs):
    try:
        with db.connection.cursor() as cursor:
            sql ="update bbs set bbs_title=%s, bbs_contents=%s, bbs_regDate=now() where bbs_key=%s"
            cursor.execute(sql, (bbs.get('bbs_title'), bbs.get('bbs_contents'), bbs.get('bbs_key')))
            db.connection.commit()
            return 'success'
    except Exception as err:
        print('수정오류', err)
        return 'fail'
    finally :
        cursor.close()

def total():
    try :
        with db.connection.cursor() as cursor:
            sql = "select count(*) bbs_total from bbs"
            cursor.execute(sql)
            row = cursor.fetchone()
            return row
    except Exception as err:
        print('게시글 개수 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()