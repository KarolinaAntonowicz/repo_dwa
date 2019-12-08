import requests

menu = ['1. Pobierz plik z internetu', '2. Zlicz liczbę liter w pobranym pliku', '3. Zlicz liczbę wyrazów w pliku',
        '4. Zlicz liczbę znaków interpunkcyjnych w pliku.', '5. Zlicz liczbę zdań w pliku',
        '6. Wygeneruj raport o użyciu liter (A-Z)', '7. Zapisz statystyki z punktów 2-5 do pliku statystyki.txt',
        '8. Wyjście z programu']
isWorking = True

text = list()


def download():
    url = 'https://s3.zylowski.net/public/input/6.txt'
    r = requests.get(url)
    filename = url.split('/')[-1]
    # zapisywanie pliku
    with open(filename, 'wb') as f:
        f.write(r.content)

    # otwieranie pliku
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