import requests
from lxml import html
from  sql_work import sql


def pats(url):
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div/div
    #//*[@id="root"]/section[2]/div[2]/div/div[2]/section/div/div
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div/div/span/text()
    #//*[@id="root"]/section[2]/div[2]/div/div[2]/section/div/div/span/text()
    request = requests.get(url)
    tree = html.document_fromstring(request.text)
    kaf = True
    i = 0
    while kaf == True:
        i += 1
        tr = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{i}]/section/div/a/h3/text()')
        date = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{i}]/section/div[1]/div/span/text()')
        if tr == []:
            break
        print(tr)
        print(date)
    fr = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[1]/a[2]/h3/text()')
    print(fr)


def pats2(url):
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[1]/a[2]/h3/text()
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[2]/a[2]/h3/text()
    #//*[@id="root"]/section[2]/div[2]/div/div[2]/section/div[1]/a[2]/h3/text()
    #
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[3]/a/h3/text()
    #//*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[4]/a/h3/text()
    #
    #//*[@id="root"]/section[2]/div[2]/div/div[2]/section/div[2]/a/h3/text()
    #//*[@id="root"]/section[2]/div[2]/div/div[2]/section/div[2]/a/h3/text()
    request = requests.get(url)
    tree = html.document_fromstring(request.text)
    big_kaf = True
    i = 0
    j = 0
    tr = ['[1']
    while big_kaf:
        kaf = True
        i += 1
        while kaf:
            j += 1
            tr = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{i}]/section/div[{j}]/a/h3/text()')
            stop = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{i + 1}]/section/div[{1}]/a/h3/text()')
            if tr == []:
                if stop == []:
                    big_kaf = False
                j = 0
                kaf = False
            else:
                data = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{i}]/section/div[{j}]/div/span/text()')
                #                   //*[@id="root"]/section[2]/div[2]/div/div[1]/section/div[2]/div/span/text()
                #                   //*[@id="root"]/section[2]/div[2]/div/div[2]/section/div[1]/div/span/text()
                print(tr, i, j)
                sql(tr, data, url)
        print(f'j = {j}', kaf)
    #tr = tree.xpath(f'//*[@id="root"]/section[2]/div[2]/div/div[{1}]/section/div[{3}]/a/h3/text()')
    #print(f'12 {tr}')


def main():
    pats2('https://lenta.ru/2021/06/08/')


if __name__ == '__main__':
    pass
    #main()