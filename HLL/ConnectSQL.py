import Tables.User as User
import pymysql
import pandas as pd
import numpy as np

"""
1. 생성자(기본)
- SQL 커넥팅하는 코드
2. Login
- 로그인 함수
3. Signup
- 회원가입 함수
4. readReview_user
- (회원)리뷰 목록 보는 함수
5. readReview_admin
- (관리자)리뷰 목록 보는 함수
6. createReview
- 리뷰 추가하는 함수
7. updateReview
- 리뷰 수정하는 함수
8. deleteReview_user
- (회원)리뷰 삭제하는 함수
9. deleteReview_admin
- (관리자)리뷰 삭제하는 함수
10. per_read_review
- 읽은 책 수 대비 리포트(double)
11. showBestseller
- 제일 많이 읽은 책 목록(list)
12. searchBookByTitle_user
- (회원) 책으로 도서관 검색(list)
13. UserBasedCollaborativeFiltering(id)
- 사용자 기반 협업 필터링
14. showBooks()
- 책 리스트 출력(번호, 제목, 작가)
"""


#1. 생성자(기본)
#- SQL 커넥팅하는 코드

db = pymysql.connect(
    user='root',
    passwd='qwerty1234',
    host='127.0.0.1',
    db='BookReview',
    charset='utf8'
)
cursor = db.cursor(pymysql.cursors.DictCursor)


#2.1 Login
#- 로그인 함수
def Login(id, passwd, admin_tf):
    # 관리자
    if admin_tf:
        sql1 = "SELECT * FROM Admin where ID='%s';" % id
        sql2 = "SELECT * FROM Admin where ID='%s' and Password='%s';" % (id, passwd)
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        if result1:
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            if result2:
                return 1;
            else:
                return -1;
        else:
                return 0;

    # 일반 사용자
    else:
        sql1 = "SELECT * FROM User where ID='%s';" % id
        sql2 = "SELECT * FROM User where ID='%s' and Password='%s';" % (id, passwd)
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        if result1:
            cursor.execute(sql2)
            result2 = cursor.fetchall()
            if result2:
                return 1;
            else:
                return -1;
        else:
            return 0;

#3. Signup
#- 회원가입 함수

def Signup(id, name, passwd):
    try:
        sql = "insert into User values('%s','%s','%s');" % (id, name, passwd)
        cursor.execute(sql)
        db.commit()
    except (pymysql.err.IntegrityError):
        return 0;
    return 1;

#4. readReview_user
#- (회원)리뷰 목록 보는 함수

def readReview_user(id):
    sql = "SELECT Pid '리뷰#', Uid '유저id', Bnum '책#', date, rating '평점', remarks '감상문' \
          FROM user, bookreport \
          where user.id=bookreport.uid and ID='%s';"% id
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)
    print(result)

#5. readReview_admin
#- (관리자)리뷰 목록 보는 함수
# 리스트를 출력하는 형태로 리턴
# 유저, 리뷰번호, 제목, 날짜, 내용

def readReview_admin():
    sql = "SELECT Pid '리뷰번호', Uid '유저아이디', Bnum '책번호', date, rating '평점', remarks '감상문' FROM bookreport;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)
    print(result)

#6. createReview
#- 리뷰 추가하는 함수

def createReview(id, bnum,date, rating, remarks):
    try:
        sql = "insert into bookreport(uid,bnum,date,rating,remarks)\
         values('%s','%d','%s','%s','%s');" % (id, bnum, date, rating, remarks)
        cursor.execute(sql)
        db.commit()
    except (pymysql.err):
        return 0;
    return 1;

#7. updateReview
#- 리뷰 수정하는 함수

def updateReview(Pid, id, date, rating, remarks):
    try:
        sql = "update bookreport \
        set date='%s', rating='%s', remarks='%s'\
        where Pid='%s';" % (date, rating, remarks, Pid)
        cursor.execute(sql)
        db.commit()
    except (pymysql.err):
        return 0;
    return 1;

#8. deleteReview_user
#- (회원)리뷰 삭제하는 함수

def deleteReview_user(id, Pid):
    sql = "delete from bookreport where Pid='%s';" % Pid
    cursor.execute(sql)
    db.commit()
    return 1;

#9. deleteReview_admin
#- (관리자)리뷰 삭제하는 함수
def deleteReview_admin(Pid):
    sql = "delete from bookreport where Pid='%s';"% Pid
    cursor.execute(sql)
    db.commit()
    return 1;

#10. per_read_review
#- 읽은 책 수 대비 리포트(double)

def per_read_review():
    sql1 = "SELECT count(*) FROM book;"
    sql2 = "SELECT count(*) FROM bookreport;"
    cursor.execute(sql1)
    book_count = cursor.fetchall()
    book_count=int(book_count[0]["count(*)"])
    cursor.execute(sql2)
    report_count=cursor.fetchall()
    report_count = int(report_count[0]["count(*)"])
    return report_count/book_count;

#11. showBestseller
#- 제일 많이 읽은 책 목록(list)

def showBestseller():
    inner_query = "select new.bnum from (SELECT bnum, count(*) from bookreview.read group by 1 limit 3) new"
    sql="select title from book where bnum in (%s)"% inner_query
    cursor.execute(sql)
    result = cursor.fetchall()
    print("1ST : "+result[0]['title'])
    print("2ND : "+result[1]['title'])
    print("3RD : "+result[2]['title'])

#12. searchBookByTitle_user
#- (회원) 책으로 도서관 검색(list)

def searchBookByTitle_user(btitle):
    sql1 = "select * from book where title='%s';"% btitle
    cursor.execute(sql1)
    result = cursor.fetchall()
    if result:
        sql2 = "select L.Name from Library L, Posses P, Book B \
        where B.Bnum=P.Bnum and L.Lnum=P.Lnum and B.title='%s'" % btitle
        cursor.execute(sql2)
        result = cursor.fetchall()
        for r in result:
            print(r['Name'], end=" ")
        print()
    else:
        print("존재하지 않는 책입니다.")

#13. UserBasedCollaborativeFiltering(id)
#- 사용자 기반 협업 필터링
from sklearn.metrics.pairwise import cosine_similarity


def findIndexByValue(arr, val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i;

def getIBydName(name):
    sql = "SELECT id FROM User where name='%s';"% name
    cursor.execute(sql)
    result = cursor.fetchall()
    result=result[0]["id"]
    return result;

def getSortedRate3ByName(df, name):
    # 책(title) 리스트
    sql5 = "SELECT title from book;"
    cursor.execute(sql5)
    result5 = cursor.fetchall()
    bnum_list2 = []
    for result in result5:
        bnum_list2.append(result['title'])


    id=getIBydName(name)
    filtered_list=df.loc[id]
    filtered_list=filtered_list.values.tolist()
    flist=[]
    for i in range(len(filtered_list[0])):
        flist.append(np.round(filtered_list[0][i],2))

    flist_copy=flist.copy()
    flist.sort(reverse=True)

    for val in flist[:3]:
        # 책 인덱스
        idx=findIndexByValue(flist_copy, val)
        print(bnum_list2[idx])


def UserBasedCollaborativeFiltering(id):
    id=int(id)
    sql1 = "SELECT Uid, Bnum, rating from bookreport;"
    cursor.execute(sql1)
    result1 = cursor.fetchall()
    result1 = pd.DataFrame(result1)

    # 사용자 수
    sql2 = "SELECT count(*) from user;"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    user_num=result2[0]["count(*)"]

    # 책 수
    sql3 = "SELECT count(*) from book;"
    cursor.execute(sql3)
    result3 = cursor.fetchall()
    book_num=result3[0]["count(*)"]

    # 사용자(id) 리스트
    sql4 = "SELECT id from user;"
    cursor.execute(sql4)
    result4 = cursor.fetchall()
    uid_list1=[]
    for result in result4:
        uid_list1.append(result['id'])

    # 사용자(name) 리스트
    sql4 = "SELECT name from user;"
    cursor.execute(sql4)
    result4 = cursor.fetchall()
    name_list = []
    for result in result4:
        name_list.append(result['name'])


    # 책(bnum) 리스트
    sql5 = "SELECT bnum from book;"
    cursor.execute(sql5)
    result5 = cursor.fetchall()
    bnum_list2 = []
    for result in result5:
        bnum_list2.append(result['bnum'])

    array=[[0]*book_num]*user_num
    ratings_df=pd.DataFrame(array, columns=[bnum_list2], index=[uid_list1])

    for k in range(len(result1)):
        ratings_df.loc[result1.loc[k][0],result1.loc[k][1]]=result1.loc[k][2]

    # 유저와 유저 간의 유사도
    user_based_collab = cosine_similarity(ratings_df, ratings_df)
    user_based_collab = pd.DataFrame(user_based_collab, index=ratings_df.index, columns=ratings_df.index)

    filtered_list=user_based_collab.loc[id]
    filtered_list=filtered_list.values.tolist()
    flist=[]
    for i in range(len(filtered_list[0])):
        flist.append(np.round(filtered_list[0][i],2))

    flist_copy=flist.copy()
    flist.sort(reverse=True)

    name=""
    bnum_list_final=[]
    for val in flist:
        if val==1.00:
            continue
        else:
            idx=findIndexByValue(flist_copy, val)
            name=User.getNameById(uid_list1[idx])
            break;

    getSortedRate3ByName(ratings_df, name)


#14. showBooks()
#- 책 리스트 출력(번호, 제목, 작가)
def showBooks():
    sql = "SELECT Bnum '책#', Author '작가', title '제목', Publisher '출판사'\
    from book;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)
    print(result)