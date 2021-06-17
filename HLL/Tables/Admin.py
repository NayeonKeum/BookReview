import pymysql

db = pymysql.connect(
    user='root',
    passwd='qwerty1234',
    host='127.0.0.1',
    db='BookReview',
    charset='utf8'
)
cursor = db.cursor(pymysql.cursors.DictCursor)

def getNameById(id):
    sql = "SELECT Name FROM Admin where ID='%s';"% id
    cursor.execute(sql)
    result = cursor.fetchall()
    result=result[0]["Name"]
    return result;