import ConnectSQL as connectSQL
import MainPage_User, MainPage_Admin

"""
0. 시간 나면 ui 툴로 만들자
1. 스플래시
- 환영환영
- 메뉴
  1) 로그인(관리자, 회원)
    - 잘못된 아이디, 잘못된 비밀번호,
    -> 로그인 후 확인!
  2) 회원가입
    - 존재하는 아이디
    -> 회원가입 후 로그인 창으로!
-

2. 메인 페이지(로그인 이후)
  1) 관리자일 경우
    - 리뷰 관리
      (1) 리뷰 목록 전체 보기
      (2) 리뷰 삭제하기-> 선택, 삭제 확인
      (3)
    - 도서관 추가
    - 책 추가
    - 도서관 재고 추가(책)->Posses 관리

  2) 회원일 경우
    - 내가 쓴 리뷰(내 보관함)
      (1) 리뷰 쓰기
      (2) 리뷰 수정하기
        - 아이디 성립시에만
      (3) 리뷰 삭제하기
        - 아이디 성립시에만
    - 책 추천(아이템 기반 협업 필터링)
    - 베스트 셀러(많이 읽은 회수*(리뷰+1) 순)
    - 책 재고 확인
      (1) 책 이름으로 어느 도서관에 존재하는지 여부 검색
"""
### 필요 변수들
id=""
passwd=""



### 스플래시


def main():
    admin_tf = False
    ## 메뉴
    while True:
        ## 환영
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("도서 리뷰 프로그램에 입장하신 것을 환영합니다.")
        # 시간 나면 앱 로고랑 같이
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("1. 회원가입하기")
        print("2. 로그인하기")
        print("3. 종료하기")
        print("++++++++++++++++++++++++++++++++++++++++++")
        num=int(input("번호를 입력해주세요. : "))
        if num==1:
            result=0
            while result!=1:
                print("회원가입 페이지입니다.")
                id = input("아이디를 입력해주세요. : ")
                name = input("이름을 입력해주세요. : ")
                passwd = input("비밀번호를 입력해주세요. : ")
                # result 1(확인),0(불가능)
                result=connectSQL.Signup(id, name, passwd)
                # 1은 가입 완료, 0은 존재하는 아이디
                if result==0:
                    print("존재하는 아이디입니다. 다시 시도해주세요")
                    print("------------------------------------------")
                    continue
            # 회원가입 성공
            print("회원가입에 성공하셨습니다. 초기 화면으로 이동합니다.")
            continue

        elif num==2:
            print("------------------------------------------")
            print("어떤 권한으로 로그인하시겠습니까?")
            print("1. 관리자")
            print("2. 일반 회원")
            print("------------------------------------------")
            login_num = int(input("번호를 입력해주세요. : "))
            result = 0
            while result != 1:
                if login_num==1:
                    admin_tf = True
                    print("관리자 로그인 페이지입니다.")
                    id=input("아이디를 입력해주세요. : ")
                    passwd=input("비밀번호를 입력해주세요. : ")
                elif login_num==2:
                    print("일반 회원 로그인 페이지입니다.")
                    id = input("아이디를 입력해주세요. : ")
                    passwd = input("비밀번호를 입력해주세요. : ")
                else:
                    print("잘못된 입력입니다. 처음으로 돌아갑니다.")
                    continue
                result=connectSQL.Login(id, passwd, admin_tf)
                if result==0:
                    print("잘못된 아이디입니다. 다시 시도해주세요")
                    continue
                elif result==-1:
                    print("잘못된 비밀번호입니다. 다시 시도해주세요")
                    continue

            # 로그인 잘 완료함
            print("로그인에 성공하셨습니다. 메인 페이지로 이동합니다!")
            # 메인 페이지(일반, 관리자)
            if admin_tf:
                MainPage_Admin.setId(id)
                MainPage_Admin.MainPage()
            else:
                MainPage_User.setId(id)
                MainPage_User.MainPage()

        elif num==3:
            print("도서 리뷰 프로그램을 종료합니다.")
            break

        else :
            print("잘못된 입력입니다! 처음으로 돌아갑니다.")
            continue
        return 0;