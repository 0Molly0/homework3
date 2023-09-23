with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    for text in file.readlines():
        if text.split(';')[5] == 'UA':
            print(text.split(';')[2])
