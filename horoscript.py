import requests
from bs4 import BeautifulSoup
from config import URLHORO

horo ={'♈️ Овен':'aries',
       '♉️ Телец':'taurus',
       '♊️ Близнецы':'gemini',
       '♋️ Рак':'cancer',
       '♌️ Лев':'leo',
       '♍️ Дева':'virgo',
       '♎️ Весы':'libra',
       '♏️ Скорпион':'scorpio',
       '♐️ Стрелец':'sagittarius',
       '♑️ Козерог':'capricorn',
       '♒️ Водолей':'aquarius',
       '♓️ Рыбы':'pisces'
}

async def get_horo(x):
    content = requests.get(URLHORO).text
    soup = BeautifulSoup(content, 'xml')
    date = soup.find_all('date')
    todaydate = str(date)[14:24]
    tomorrowdate = str(date)[36:46]
    tomorrowdate2 = str(date)[60:70]
    try:
        print(horo[x])
        horosoup = soup.find_all(horo[x])
        for item in horosoup:
            today = item.find('today').text
            tomorrow = item.find('tomorrow').text
            tomorrow2 = item.find('tomorrow02').text
        y = f'🔯<b>Гороскоп на сегодня\n\n{x} на {todaydate}</b>{today}\n<b>{x} на завтра {tomorrowdate}</b>{tomorrow.replace('Сегодня','Завтра').replace('сегодня','завтра')}\n<b>{x} на послезавтра {tomorrowdate2}</b>{tomorrow2.replace('Сегодня','Послезавтра').replace('сегодня','послезавтра')}\n'
    except:
        y = 'Воспользуйтесь клавиатурой'
    return y