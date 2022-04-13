class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")
        
        cls.younghoon_name = parameter_list[0]
        cls.younghoon_email = parameter_list[1]
        cls.younghoon_password = parameter_list[2]

        younghoon = User(cls.younghoon_name, cls.younghoon_email, cls.younghoon_password)
        return younghoon
        
    @classmethod
    def from_list(cls, list_params):
        cls.yoonsoo_name = list_params[0]
        cls.yoonsoo_email = list_params[1]
        cls.yoonsoo_password = list_params[2]

        yoonsoo = User(cls.yoonsoo_name, cls.yoonsoo_email, cls.yoonsoo_password)
        return yoonsoo

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)