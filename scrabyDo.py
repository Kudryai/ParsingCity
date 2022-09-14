from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import re
import csv


class ScrapyDo:

    def MOEX():
        result = []
        site = 'https://smart-lab.ru/q/index_stocks/IMOEX/'
        hdr = {'User-Agent': 'Mozilla/6.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'lxml')
        cnt = 25
        dates2 = soup.find(class_='simple-little-table trades-table').find_all('tr')
        for ves in dates2:
            prod = ves.find_all('td')
            if len(prod) != 0:
                vesimoex = prod[3].text
                price = prod[6].text
                yty = re.sub(r'%','',prod[10].text)
                result.append([cnt, prod[2].text, re.sub(r'/forum/','',prod[2].find('a')['href']),
                re.sub(r'%','',vesimoex),price,yty])
                cnt += 1
        return ScrapyDo.divOK(result)

    def divOK(data):
        site = 'https://vsdelke.ru/dividendy/kalendar-vyplat-rossiyskih-kompaniy-2022.html'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(site,headers=hdr)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'lxml')
        div = soup.find_all('tr')
        check = set()
        result = {}
        for items in div:
            divos = items.find_all('td')
            try:
                for indx in divos:
                    for j in range(len(data)):
                        if data[j][2] in indx.text:
                            check.add(j)
                            num_div = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?",divos[2].text)
                            result[data[j][2]] = result.get(data[j][2], float(num_div[0]))
            except:
                continue
        check = sorted(check)
        for k in range(len(data)):
            if k not in check:
                result[data[k][2]] = result.get(data[k][2],0)
            data[k].append(result[data[k][2]])
        return data



# Запись в CSV.

# for num in ScrapyDo.MOEX():
#     with open('/mnt/c/Users/user/Desktop/Parsing/ParsingCity/DataInvest/ct.csv','a',encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow((num[0],num[1],num[2],num[3],num[4],num[5],num[6]))

