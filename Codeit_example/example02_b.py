from abc import ABC, abstractclassmethod

class Keyboard:
    @abstractclassmethod
    def save_input(self, content: str) -> None:
        """키보드 인풋 저장 메소드"""
        pass

    @abstractclassmethod
    def send_input(self) -> str:
        """키보드 인풋 전송 메소드"""
        pass


class AppleKeyboard(Keyboard):
    """애플 키보드 클래스"""

    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.keyboard_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class SamsungKeyboard(Keyboard):
    """삼성 키보드 클래스"""
    def __init__(self):
        self.user_input = ""

    def save_input(self, input):
        self.user_input = input

    def send_input(self):
        return self.user_input