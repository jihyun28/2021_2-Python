import random # 랜덤 모듈 사용

score = [] # score 기록 저장되는 배열

# 종료될 때까지 무한 반복
while(True):

    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1.게임시작 2. 기록확인 3. 게임종료")
    n = input(">> ") # input() 함수를 통해 입력받은 값을 변수에 저장
            
    if (n == "1"):
        r = random.randrange(1, 101, 1) # 랜덤 숫자 생성
        num = -1 # num 값 초기화
        cnt = 1 # 시도 횟수
        a = 1 # 시작하는 범위값 초기화
        b = 100 # 마지막 범위값 초기화

        # r이 num과 같을 때까지 반복
        while(r != num):

            num = int(input('%d번째 숫자 입력(%d,%d) : ' %(cnt,a,b))) # input() 함수를 이용하여 원하는 수 입력 

            # 랜덤값(정답값)이 입력한 숫자보다 작은 경우
            if (r < num): 
                print("DOWN")
                b = num - 1
                cnt += 1

            # 랜덤값(정답값)이 입력한 숫자보다 큰 경우        
            elif (r > num):
                print("UP")
                cnt += 1
                a = num + 1

            # # 랜덤값(정답값)이 입력한 숫자와 같은 경우
            elif (r == num):
                print("정답입니다!!")
                print(cnt, "번째만에 맞추셨습니다.")
                score.append(cnt) # 정답인 경우 score 배열에 기록 추가
                break
            
        print("정답입니다!!")
        print(cnt, "번째만에 맞추셨습니다.")    

    # score 배열에 저장된 기록 출력
    elif (n == "2"):
        score.sort() # score 안에 있는 배열 값을 오름차순으로 정렬
        for i in range(len(score)):
            print(i+1," ",score[i-1])
        break

    # 게임종료
    elif n == "3":
        break
    
    else:
        print("error")
