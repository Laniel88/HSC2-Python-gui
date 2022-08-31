import ssl
import time
import requests
from urllib import request
from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager
from component import resource_path

ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_SSLv23)
ctx.set_ciphers('SSLv3')
context_ssl = ssl._create_unverified_context()

def getReSoup(reNum):
    baseURL = 'https://www.hanyang.ac.kr/web/www/'
    reURL = ['re1', 're2', 're4']

    url = baseURL + reURL[reNum]
    # get soup

    def getRequest(cnt=0):
        cnt += 1
        # get from user_agent.txt
        response = requests.get(url, headers={'User-Agent': 'Custom'})
        if response.status_code == 404:
            return getRequest(cnt)
        else:
            return response, cnt

    response, cnt = getRequest()
    print('{} >> try : {}'.format(response, cnt))
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def getRequestsInfinite(url, cnt=0):
    cnt += 1
    try:
        response = request.urlopen(url,context= context_ssl)
        return response, cnt
    except:
        return getRequestsInfinite(url, cnt)


def getReList(reNum):

    def heAppend(soup, tag):
        def readImgURL(URL):
            if URL == '/html-repositories/images/custom/food/no-img.jpg':
                img = open(resource_path('img/noImage.jpeg'), 'rb').read()
                return img
            else:
                img, cnt = getRequestsInfinite(URL)
                print('Image request has occurred - attempts : {} tries'.format(cnt))
                img = img.read()
                return img

        def menuToList(menuOriginStr):
            try:
                for i in range(len(menuOriginStr)):
                    if menuOriginStr[i] == ']':
                        blanknum = i
                title = menuOriginStr[0:blanknum + 1]
                menuList = menuOriginStr[blanknum + 2:].split(', ')
                menuList.insert(0, title)
                return menuList
            except UnboundLocalError:
                return [False] + menuOriginStr.split(', ')

        tempList = []
        tempList.append(readImgURL(soup.find('img').get('src')))
        tempList.append(menuToList(soup.find('img').get('alt')))
        tempList.append(soup.find('p', class_='price').get_text())
        tempList.append(tag)

        return tempList
    foodBoxList = getReSoup(reNum) \
        .find('div', class_='foodView-view') \
        .find("div", class_='box tab-box-wrap tab-dth1 tab-lg', id='_foodView_WAR_foodportlet_tab_1') \
        .find("div", class_='tab-pane active', id='messhall1') \
        .find_all('div', class_='in-box')

    reList = []

    for box in foodBoxList:
        tag = box.find('h4', class_='d-title2').get_text()
        sortedSoup = box.findAll('li', class_="span3")
        for i in range(len(sortedSoup)):
            reList.append(heAppend(sortedSoup[i], tag))

    return reList


def getAllreList(process=5):
    try:
        finalReList = Manager().list()
        start_time = time.time()
        pool = Pool(processes=process)

        # multiprocessing
        finalReList.append(pool.map(getReList, [0, 1, 2]))

        # # Sequential crawling
        # finalReList.append(getReList(0))
        # finalReList.append(getReList(1))
        # finalReList.append(getReList(2))
        pool.close()
        pool.join()

        seq = time.time() - start_time

        # unwraping list (only when multiprocessing is used)
        finalReList = finalReList[0]

        re0Num = len(finalReList[0])
        re1Num = len(finalReList[1])
        re2Num = len(finalReList[2])

        print("All data loaded successfully in : {} sec".format(round(seq,3)))
        return (finalReList, (re0Num, re1Num, re2Num))

    except RecursionError:
        return ('WEB ERROR', 'Continuous Web Call Error')

    except Exception as e:
        return ('WEB ERROR', str(e))
