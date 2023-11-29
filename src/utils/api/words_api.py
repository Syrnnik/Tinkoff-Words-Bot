import requests
from bs4 import BeautifulSoup


def get_today_word():
    print("Start getting today word")
    response = requests.get(
        url="https://wotpack.ru/slova-iz-5-bukv-tinkoff-otvety-na-segodnja-nojabr/"
    )
    page = BeautifulSoup(response.text, 'lxml')
    ul = page.select('div.content-inner.jeg_link_underline ul')[1]
    li = ul.select('li')[0]
    word = li.text.split(' ')[3].replace('.', '')
    print(f"Today word is {word}")
    return word


if __name__ == "__main__":
    word = get_today_word()
    print(word)
