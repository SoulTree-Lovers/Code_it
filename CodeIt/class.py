class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1
    
    def __str__(self):
        return "사용자:{}, 이메일:{}, 비밀번호:{}".format(self.name, self.email, self.pw)

