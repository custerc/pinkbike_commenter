from bs4 import BeautifulSoup
import requests
import time

# PARAMETERS TO CHANGE
bike = "forbidden druid"
region = "3"
size = "23,27,34,35,36,30,31,47"
counter = 0


def bikefinder(bike, region, size):
    while counter < 144:
        bike = bike.replace(' ', '%20')
        url = 'https://www.pinkbike.com/buysell/list/?region={}&q={}&framesize={}'.format(
            region, bike, size)

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        items = []
        for item in soup.find_all('a', style="font-size: 18px;font-weight:bold;color:#000000"):
            items.append([item.get_text(), item['href']])
        items_merged = [','.join(item) for item in items]

        with open('bikes.txt', 'r+') as file:
            for bike in items_merged:
                for line in file:
                    if bike in line:
                        break
                else:
                    file.write(bike)
                    file.write('\n')
                    print('Found a new bike!!!')
                    print(bike)
                    time.sleep(15)
                    print('Found a new bike!!!')
                    print(bike)
                    time.sleep(15)
                    print('//////////////////////////////////////////')
        time.sleep(600)


bikefinder(bike, region, size)
