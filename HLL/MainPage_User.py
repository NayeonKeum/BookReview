import Tables.User as User
import Tables.BookReport as BookReport
import ConnectSQL as connectSQL
import Main
import datetime

### 메인 페이지
id=""

def setId(nid):
    global id
    id=nid

def MainPage():
    while True:
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("사용자 메인 페이지 : "+User.getNameById(id))
        print("++++++++++++++++++++++++++++++++++++++++++")
        User.delayed_report(id)
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("1. 내가 쓴 리뷰")
        print("2. 리뷰 쓰기")
        print("3. 리뷰 수정하기")
        print("4. 리뷰 삭제하기")
        print("5. 책 재고 확인하기")
        print("6. 맞춤형 책 추천받기")
        print("7. 베스트 셀러 보기")
        print("8. 시작 페이지로 돌아가기")
        print("++++++++++++++++++++++++++++++++++++++++++")
        num = int(input("번호를 입력하세요. : "))
        #내가 쓴 리뷰
        if num == 1:
            connectSQL.readReview_user(id)
        #리뷰 쓰기
        elif num == 2:
            # date
            now = datetime.datetime.now()
            date = now.strftime('%Y-%m-%d')
            # btitle
            print("-------------------------------------------")
            print("리뷰를 작성할 수 있는 책 리스트")
            connectSQL.showBooks()
            print("-------------------------------------------")
            bnum=int(input("리뷰를 작성할 책의 번호를 입력하세요 : "))
            # rating
            rating = float(input("점수를 매겨주세요(1~5) : "))
            # remarks
            remarks = input("리뷰를 작성해주세요 : ")
            connectSQL.createReview(id, bnum, date, rating, remarks)
        #리뷰 수정하기
        elif num == 3:
            # Pid
            Pid = input("수정할 리뷰의 번호를 입력하세요. : ")
            result = BookReport.isMyReport(id, Pid)
            if result:
                # date
                now = datetime.datetime.now()
                date = now.strftime('%Y-%m-%d')
                # rating
                rating = float(input("점수를 매겨주세요(1~5) : "))
                # remarks
                remarks = input("리뷰를 작성해주세요 : ")
                connectSQL.updateReview(Pid, id, date, rating, remarks)
                print("수정되었습니다.")
            else:
                print("본인이 소유하고 있는 리뷰가 아닙니다. 처음으로 돌아갑니다.")
                continue

        #리뷰 삭제하기
        elif num == 4:
            # Pid
            Pid = input("삭제할 리뷰의 번호를 입력하세요 : ")
            # t/f
            result=BookReport.isMyReport(id, Pid)
            if result:
                connectSQL.deleteReview_user(id, Pid)
                print("삭제되었습니다.")
            else:
                print("본인이 소유하고 있는 리뷰가 아닙니다. 처음으로 돌아갑니다.")
                continue
        #책 재고 확인하기
        elif num == 5:
            # btitle
            btitle = input("재고가 있는 도서관을 확인할 책 제목을 입력해주세요 : ")
            connectSQL.searchBookByTitle_user(btitle)
        #맞춤형 책 추천받기
        elif num == 6:
            print("사용자 기반 협업 필터링의 결과입니다.")
            connectSQL.UserBasedCollaborativeFiltering(id)
        #베스트 셀러 보기
        elif num == 7:
            print("현재 베스트 셀러 리스트입니다.")
            connectSQL.showBestseller()
        #시작 페이지로 돌아가기
        elif num == 8:
            print("시작 페이지로 돌아갑니다.")
            Main.main()
            break
        else:
            print("잘못 입력하셨습니다. 다시 선택해주세요.")
            continue



