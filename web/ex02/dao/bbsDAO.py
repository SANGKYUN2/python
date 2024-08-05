from dao import db

def bbs_List(args) :
    page = int(args.get('page'))
    size = int(args.get('size'))
    start = (page - 1) * size
    try :
        with db.connection.cursor() as cursor:
            sql = 'select * from bbs order by bbs_key desc limit %s, %s'
            cursor.execute(sql, (start, size))
            return cursor.fetchall()
    except Exception as err :
        print ('게시글 목록 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def bbs_Total() :
    try :
        with db.connection.cursor() as cursor:
            sql = 'select count(*) bbs_Total from bbs'
            cursor.execute(sql)
            return cursor.fetchone()
    except Exception as err :
        print('게시글 개수 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def bbs_Insert(bbs) :
    try :
        with db.connection.cursor() as cursor :
            sql = 'insert into bbs(bbs_writer, bbs_title, bbs_contents) values (%s, %s, %s)'
            cursor.execute(sql, (bbs.get('bbs_writer'), bbs.get('bbs_title'), bbs.get('bbs_contents')))
            db.connection.commit()
            return "success"
    except Exception as err :
        print("게시글 등록 오류 : ", err)
        return "fail"
    finally :
        cursor.close()

def bbs_Delete(bbs_key) :
    try :
        with db.connection.cursor() as cursor :
            sql = "delete from bbs where bbs_key=%s"
            cursor.execute(sql, bbs_key)
            db.connection.commit()
            return 'success'
    except Exception as err :
        print('게시글 삭제 오류 : ', err)
        return 'fail'
    finally :
        cursor.close

def bbs_Read(bbs_key) :
    try :
        with db.connection.cursor() as cursor :
            sql = 'select * from bbs where bbs_key=%s'
            cursor.execute(sql, bbs_key)
            row = cursor.fetchone()
            return row
    except Exception as err:
        print('게시글 읽기 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()

def bbs_Update(bbs) :
    try :
        with db.connection.cursor() as cursor :
            sql = "update bbs set bbs_title=%s, bbs_contents=%s, bbs_regDate=now() where bbs_key=%s" 
            cursor.execute(sql, (bbs.get('bbs_title'), bbs.get('bbs_contents'), bbs.get('bbs_key')))
            db.connection.commit()
            return 'success'
    except Exception as err :
        print('게시글 수정 오류 : ', err)
        return 'fail'
    finally :
        cursor.close()