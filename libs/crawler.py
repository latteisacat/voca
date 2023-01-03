import requests


def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content  # .text와 달리 content는 디코딩이 되지 않은상태의 html을 그대로 보여주므로 프로그램이 처리하기 용이함.
