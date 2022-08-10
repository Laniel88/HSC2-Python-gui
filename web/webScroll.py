import time
import requests

from bs4 import BeautifulSoup
from multiprocessing import Pool, Manager

def getReSoup(reNum):
    baseURL = 'https://www.hanyang.ac.kr/web/www/'
    reURL = ['re1','re2','re4']

    url = baseURL + reURL[reNum]

    #get soup
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup



def getReList(reNum):
    ## <--                        --> ##
    def heAppend(soup):
        def imgURL(URL):
            if URL == '/html-repositories/images/custom/food/no-img.jpg':
                return 'https://www.hanyang.ac.kr/html-repositories/images/custom/food/no-img.jpg'
            else:
                return URL
        
        def menuToList(menuOriginStr):
            try:
                for i in range(len(menuOriginStr)):
                    if menuOriginStr[i] == ']':
                        blanknum = i
                title = menuOriginStr[0:blanknum+1]
                menuList = menuOriginStr[blanknum+2 :].split(', ')
                menuList.insert(0,title)
                return  menuList
            except UnboundLocalError:
                return [False]+menuOriginStr.split(', ')


        tempList = []
        tempList.append(imgURL(soup.find('img').get('src')))
        tempList.append(menuToList(soup.find('img').get('alt')))
        tempList.append(soup.find('p',class_ = 'price').get_text())
        
        return tempList
    ## <--                        --> ##

    sortedSoup = getReSoup(reNum).find("div",class_='box tab-box-wrap tab-dth1 tab-lg',id = '_foodView_WAR_foodportlet_tab_1') \
                            .find("div",class_ = 'tab-pane active', id ='messhall1' ).findAll('li', class_="span3")


    reList = []

    for i in range(len(sortedSoup)):
        reList.append(heAppend(sortedSoup[i]))

    return reList

def getAllreList(process = 4):
    try:
        finalReList = Manager().list()
        start_time = time.time()
        pool = Pool(processes = process)
        finalReList.append(pool.map(getReList,[0,1,2]))
        pool.close()
        pool.join()

        seq = time.time()-start_time


        finalReList = finalReList[0]

        re0Num = len(finalReList[0])
        re1Num = len(finalReList[1])
        re2Num = len(finalReList[2])
        
        print("[log.d] web loaded with time : {}".format(seq))
        return (finalReList, (re0Num,re1Num,re2Num))
    except Exception as e:
        return ('WEB ERROR',str(e))
    