import pymysql
import pandas as pd

db = pymysql.connect(
    user='root',
    passwd='qwerty1234',
    host='127.0.0.1',
    db='BookReview',
    charset='utf8'
)
cursor = db.cursor(pymysql.cursors.DictCursor)

def getNameById(id):
    sql = "SELECT Name FROM User where ID='%s';"% id
    cursor.execute(sql)
    result = cursor.fetchall()
    result=result[0]["Name"]
    return result;


def getIBydName(name):
    sql = "SELECT id FROM User where name='%s';"% name
    cursor.execute(sql)
    result = cursor.fetchall()
    result=result[0]["id"]
    return result;


def getTitleByBnum(bnum):
    sql = "SELECT title FROM book where bnum='%s';"% bnum
    cursor.execute(sql)
    result = cursor.fetchall()
    result=result[0]["title"]
    return result;


# 테이블 네 개 조인
# 평균적으로 책을 읽고 리뷰 쓰는 데 걸리는 시간!
def delayed_report_df(id):
    name_list=[]
    title_list=[]
    numof_report_not_written_list=[]
    sql="select distinct table1.id, table2.bnum, datediff(table2.date, table1.date) dd from (select user.id, book.bnum, r.date from user, book, bookreview.read r where r.uid = user.id and r.bnum = book.bnum) table1, (select user.id, book.bnum, bookreport.date from user, book, bookreport where bookreport.uid=user.id and bookreport.bnum=book.bnum) table2 where table1.id=table2.id and table1.bnum=table2.bnum"
    cursor.execute(sql)
    result = cursor.fetchall()
    result=pd.DataFrame(result)
    id=int(id)
    for i in range(len(result)):
        if (result.loc[i,'id']==id):
            bnum=result.loc[i,'bnum']
            dd=result.loc[i,'dd']
            name_list.append(getNameById(id))
            title_list.append(getTitleByBnum(bnum))
            numof_report_not_written_list.append(dd)
    name_list = pd.DataFrame(name_list)
    title_list = pd.DataFrame(title_list)
    numof_report_not_written_list = pd.DataFrame(numof_report_not_written_list)
    result_df = pd.concat([name_list, title_list, numof_report_not_written_list], axis=1)
    return result_df


def delayed_report(id):
    df=delayed_report_df(id)
    for i in range(len(df)):
        print("%s을(를) 읽고 리뷰를 작성하는 데 %d일이 걸렸습니다, 고객님."%(df.iloc[i,1],df.iloc[i,2]))

