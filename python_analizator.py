import requests

menu = ['1. Pobierz plik z internetu', '2. Zlicz liczbę liter w pobranym pliku', '3. Zlicz liczbę wyrazów w pliku',
        '4. Zlicz liczbę znaków interpunkcyjnych w pliku.', '5. Zlicz liczbę zdań w pliku',
        '6. Wygeneruj raport o użyciu liter (A-Z)', '7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt',
        '8. Wyjście z programu']
isWorking = True

text = list()


def download():
    print('Download Starting...')
    url = 'https://s3.zylowski.net/public/input/6.txt'
    r = requests.get(url)
    filename = url.split('/')[-1]
    # writing file
    with open(filename, 'wb') as f:
        f.write(r.content)

    # open file
    file = open(filename, 'r')
    text = list(file)
    # text = file.read()
    file.close()
    return text


text = download()

def countWords(text):
    for line in text:
        wordslist = line.split()
        words = len(wordslist)
    return words

def countLetters(text, printing):
    x = [None] * 26
    for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for line in text:
            # print(line.count(letter))
            x[i] = line.count(letter)
            x[i] += line.count(letter.lower())
        if printing == True:
            print(letter, ': ', x[i])
    # print(x)
    return sum(x)

def countPunctations(text):
    full_stops = 0
    commas = 0
    semicolon = 0
    exclamation_mark = 0
    question_mark = 0
    dash = 0
    colon = 0
    ellipsis = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        commas = commas + len(line.split(','))
        semicolon = semicolon + len(line.split(';'))
        exclamation_mark = exclamation_mark + len(line.split('!'))
        question_mark = question_mark + len(line.split('?'))
        dash = dash + len(line.split('-'))
        colon = colon + len(line.split(':'))
        ellipsis = ellipsis + len(line.split('...'))
    return full_stops + commas + semicolon + exclamation_mark + question_mark + dash + colon + ellipsis

def countSentences(text):
    full_stops = 0
    exclamation_mark = 0
    question_mark = 0
    ellipsis = 0
    for line in text:
        full_stops = full_stops + len(line.split('.'))
        ellipsis = ellipsis + len(line.split('...'))
        exclamation_mark = exclamation_mark + len(line.split('!'))
        question_mark = question_mark + len(line.split('?'))
    return full_stops + exclamation_mark + question_mark + ellipsis

while (isWorking):
    for element in menu:
        print(element)
    action = int(input())
