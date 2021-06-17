import Tables.Admin as Admin
import ConnectSQL as connectSQL
import Main

### 메인 페이지
id=""

def setId(nid):
    global id
    id=nid


def MainPage():
    while True:
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("관리자 메인 페이지 : "+Admin.getNameById(id))
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("현재 읽은 책 수 대비 리뷰 개수 : "+str(connectSQL.per_read_review()))
        print("------------------------------------------")
        print("1. 리뷰 전체 보기")
        print("2. 리뷰 삭제하기")
        print("3. 시작 페이지로 돌아가기")
        print("++++++++++++++++++++++++++++++++++++++++++")
        num=int(input("번호를 입력하세요. : "))
        if num==1:
            connectSQL.readReview_admin();
        elif num==2:
            result=0
            while result!=1:
                Pid=input("삭제하고자하는 리뷰의 번호를 입력하시오 : ")
                result=connectSQL.deleteReview_admin(Pid)

        elif num==3:
            print("시작 페이지로 돌아갑니다.")
            Main.main()
            break
        else:
            print("잘못 입력하셨습니다. 다시 선택해주세요.")
            continue





