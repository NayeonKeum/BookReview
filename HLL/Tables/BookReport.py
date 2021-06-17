import pymysql

db = pymysql.connect(
    user='root',
    passwd='qwerty1234',
    host='127.0.0.1',
    db='BookReview',
    charset='utf8'
)
cursor = db.cursor(pymysql.cursors.DictCursor)

def isMyReport(id, Pid):
    sql = "SELECT * FROM BookReport where uid='%s' and Pid='%s';"% (id, Pid)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        return True;
    else:
        return False;