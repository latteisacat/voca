import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


class Searcher:

    def __init__(self, search_list, web_driver_path):
        self.search_list = search_list
        self.voca_list = list()
        self.driver = webdriver.Chrome(
            executable_path=web_driver_path
            # 경로지정 시 유의사항
            # 해당 모듈을 호출하는 main.py기준으로 경로 지정
        )

    # html헤더만 가져오고 바디를 가져오지 못함. 아마도 데이터를 가져와 화면에 표시하는 부분이
    # 따로 존재하는 것으로 보임.
    # html 헤더에서 host를 찾아야 함. 그냥 selenium쓰면 다되네?
    def word_search(self):
        for word in self.search_list:
            url = f"https://en.dict.naver.com/#/search?range=all&query={word}"
            self.driver.get(url)  # 주소를 입력하고 enter를 치는 효과가 있음
            sleep(2)
            page_string = self.driver.page_source
            # 네이버 사전은 그냥 수집해도 잘 되는데 인스타 같은 경우 모든 소스를 받아오기까지 추가적인 시간이 필요한가보다. 혹시모르니 sleep을 걸어주자.
            doc = BeautifulSoup(page_string, 'html.parser')
            main_meaning = str(doc.select('div.row')[0])
            doc = BeautifulSoup(main_meaning, 'html.parser')
            num = doc.select('div.row > ul.mean_list > li.mean_item > span.num')
            basic_word = doc.select('div.row > div.origin > a.link > strong.highlight')[0].get_text().strip()
            counter = 1 if len(num) == 0 else len(num)
            mean_list = list()
            for i in range(counter):
                # 유니코드 2219번을 인식하지 못하여 *기호로 대체
                meaning = doc.select('div.row > ul.mean_list > li.mean_item > p.mean')[i].get_text().strip().replace("\t", "").replace("∙", "*").splitlines()
                if len(meaning) == 3:
                    meaning.pop(1)
                mean_list.append(meaning)
            self.voca_list.append([basic_word, mean_list])
        self.driver.close()

    # 모든 전처리 과정을 끝내고 csv파일로 변경하려고보니 2차원 리스트가 아님. 2차원 리스트 형태로의 수정 필요.
    def convert_to_2d_list(self):
            object = self.voca_list.copy()
            list_2d = list()
            for i in range(len(object)):
                word = object[i][0]
                list_1d = list()
                for j in range(len(object[i][1])):
                    if len(object[i][1][j]) == 2:
                        parts_of_speech = object[i][1][j][0]
                        meaning = object[i][1][j][1]
                    elif len(object[i][1][j]) == 1:
                        parts_of_speech = ""
                        meaning = object[i][1][j][0]
                    if j == 0:
                        list_1d.extend([word, parts_of_speech, meaning])
                        list_2d.append(list_1d)
                        list_1d = list()
                    else:
                        list_1d.extend(["", parts_of_speech, meaning])
                        list_2d.append(list_1d)
                        list_1d = list()
            self.voca_list = list_2d.copy()




