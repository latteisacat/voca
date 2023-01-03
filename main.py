from wordlist import reader
from wordlist import searcher

search_data = reader.Reader("C:\\developer\\voca\\eng.txt")

search_data.read_data()
search_data.remove_stopwords()
print(search_data.data)

dic_word = searcher.Searcher(search_data.data)  # searcher.Searcher(["added"])
dic_word.word_search()
print(dic_word.voca_list)
