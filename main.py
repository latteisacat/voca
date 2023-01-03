from wordlist import reader
from wordlist import searcher
from libs import list_to_csv

search_data = reader.Reader("C:\\developer\\voca\\eng.txt")

search_data.read_data()
search_data.remove_stopwords()
print(search_data.data)

dic_word = searcher.Searcher(search_data.data)
dic_word.word_search()
print(dic_word.voca_list)
dic_word.convert_to_2d_list()
print(dic_word.voca_list)
list_to_csv.list_to_csv(dic_word.voca_list, 'C:/developer/voca/voca_list.csv')
