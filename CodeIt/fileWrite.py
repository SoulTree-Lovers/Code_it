with open("vocabulary.txt", 'a', encoding="UTF-8") as f:

    while 1:
        eng = input("영어 단어를 입력하세요: ")
        if eng == "q":
            break
        
        else:
            kor = input("한국어 뜻을 입력하세요: ")
            f.write(eng + ": ")
            f.write(kor + "\n")

        
        