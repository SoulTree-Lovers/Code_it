import requests

### 코드를 작성하세요 ###
# https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=2

rating_pages = []

for a in range(3):
    for b in range(1, 13):
        for c in range(5):
            url = "https://workey.codeit.kr/ratings/index?year={}&month={}&weekIndex={}".format(a+2010, b, c)
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)



# 출력 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드