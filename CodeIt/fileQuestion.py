with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    
    voca_list = [i.strip().split(": ") for i in f]
    for i in range(len(voca_list)):
        answer = input("{}:".format(voca_list[i][1]))
        correct_answer = voca_list[i][0]
        if answer == correct_answer:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(correct_answer))
    