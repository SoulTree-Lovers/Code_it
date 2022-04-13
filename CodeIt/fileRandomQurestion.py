from random import *

with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    
    voca_list = [i.strip().split(": ") for i in f]          # 단어장을 읽어서 리스트로 변환
    voca_dict = {}                                          # 빈 딕셔너리 생성
    for i in range(len(voca_list)):                         # voca_list를 딕셔너리로 변환
        voca_dict[voca_list[i][1]] = voca_list[i][0]        # voca_list를 딕셔너리로 변환

    keys_list = list(voca_dict)                             # 딕셔너리의 키를 리스트로 변환
    values_list = list(voca_dict.values())                  # 딕셔너리의 값을 리스트로 변환


    while True:
        rand_int = randint(0, len(voca_dict)-1)             # 0부터 7까지 랜덤수 생성
        answer = input("{}:".format(keys_list[rand_int]))   # 사용자에게 정답을 입력받음
        correct_answer = values_list[rand_int]              # 정답을 변수에 저장

        if answer == correct_answer:                        # 정답 입력 시 "맞았습니다!" 출력
            print("맞았습니다!")
        elif answer == ("q" or "Q"):                            # q나 Q를 입력 시 반복문 종료
            break
        else:                                               # 오답 입력 시 정답을 알려줌
            print("아쉽습니다. 정답은 {}입니다.".format(correct_answer))
