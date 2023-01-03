import csv

fields = ["단어", "품사", "뜻"]


def list_to_csv(list_2d, save_location):
    with open(save_location, 'w', encoding='cp949', newline='') as file:
        write = csv.writer(file)
        write.writerow(fields)
        write.writerows(list_2d)


