# 1. 입력한 영어 데이터를 토크나이징 시켜 저장
import nltk
import re


class Reader:
    # 생성자
    def __init__(self, filename):
        self.data = None
        self.filename = filename

    # 특수문자 제거
    def read_data(self):
        with open(self.filename, 'r', encoding='UTF-8') as eng_text:
            self.data = re.sub(r"[^a-zA-Z]", " ", eng_text.read())

    # 추출한 데이터 확인용 함수, just for debugging
    def print_data(self):
        print(self.data)

    # 불용어 및 고유명사 제거, 단어 빈도 수 대로 정렬
    def remove_stopwords(self):
        no_stopword_list = list()
        stop_words = set(nltk.corpus.stopwords.words('english'))
        tagged_data = nltk.tag.pos_tag(self.data.split())
        edited_data = [word for word, tag in tagged_data if tag != 'NNP' and tag != 'NNPS']
        self.data = edited_data

        for word in self.data:
            if not word.lower() in stop_words:
                no_stopword_list.append(word)
        sorted_data = sorted(no_stopword_list, key=lambda x: (-no_stopword_list.count(x), no_stopword_list.index(x)))
        self.data = list(dict.fromkeys(sorted_data))


test = Reader("C:\\developer\\voca\\eng.txt")
test.read_data()
test.remove_stopwords()
test.print_data()
