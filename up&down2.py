import random # 랜덤 모듈 사용
from datetime import datetime # 날짜 기록하기 위해 모듈 사용

score = [] # score 기록 저장되는 배열

# 종료될 때까지 무한 반복
while(True):

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임시작 2. 기록확인 3. 게임종료")
    n = input(">> ") # input() 함수를 통해 입력받은 값을 변수에 저장

    try: # 보기에 없는 번호를 입력했을 때의 예외처리
        if (n == "1"):
            r = random.randrange(1, 101, 1) # 랜덤 숫자 생성
            num = -1 # num 값 초기화
            cnt = 1 # 시도 횟수
            a = 1 # 시작하는 범위값 초기화
            b = 100 # 마지막 범위값 초기화
            f = open('C:/Users/user/Desktop/up&down_list.txt', 'w')

            # r이 num과 같을 때까지 반복
            while(r != num):

                num = int(input('%d번째 숫자 입력(%d,%d) : ' %(cnt,a,b))) # input() 함수를 이용하여 원하는 수 입력 

                # 정답으로 1~100 범위 안에 해당하는 숫자만 입력하게 하도록 함
                if (num < 1 or num > 100):
                    print("1부터 100까지의 숫자만 입력해주세요")
                else:
                    # 랜덤값(정답값)이 입력한 숫자보다 작은 경우
                    if (r < num):
                        # 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 함
                        if (num > b):
                            print("범위가 맞지 않습니다. 다시 입력해주세요.")
                        else:
                            print("DOWN")
                            b = num - 1
                            cnt += 1

                    # 랜덤값(정답값)이 입력한 숫자보다 큰 경우        
                    elif (r > num):
                        # 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 함
                        if ( num < a):
                            print("범위가 맞지 않습니다. 다시 입력해주세요.")
                        else:
                            print("UP")
                            cnt += 1
                            a = num + 1

                    # # 랜덤값(정답값)이 입력한 숫자와 같은 경우
                    elif (r == num):
                        print("정답입니다!!")
                        print(cnt, "번째만에 맞추셨습니다.")
                        # 최고기록인 경우에만 기록에 추가ㅣ
                        if(len(score) == 0 or score[0][0] > cnt): #len(score)==0은 리스트가 비어있는 경우를 뜻함
                            print("최고기록 갱신~!")
                            name = input('닉네임을 입력해주세요 : ')
                            time = datetime.now() # 현재 시간 저장
                            score.insert(0,(cnt, name, time.strftime('%Y-%m-%d %H:%M:%S'))) #횟수, 닉네임, 날짜를 튜플로 저장
                            for i in range(len(score)): # 파일 쓰기를 할 때 list의 모든 요소는 문자여야 한다.
                                score[i] = str(score[i])
                            f.write(''.join(score)) # join() 함수를 사용하여 string으로 형변환 가능, 파일 쓰기 가능
                            
        # score 배열에 저장된 기록 출력
        elif (n == "2"):
            for i in range(len(score)):
                print(i+1," ",score[i])
           
        # 게임종료
        elif n == "3":
            f.close() # 파일 내용 저장 후 종료
            break

        else:
            raise
    
    except: # 예외 발생 시 다음 문구 출력
        print("error")
        print("보기에 있는 숫자만 골라주세요")
