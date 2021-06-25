import requests
from lxml import html
from  sql_work import sql


def pats(url, headers):
    # headline, discription, url, somphing
    # headline
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1/text()
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1
    # discription
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[3]/div[9]/text()

    print(f'work with url:{url}')
    try:
        response = requests.get(url, headers=headers)
        tree = html.document_fromstring(response.text)
        headlines = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1/text()')
        discription = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')
        if headlines == []:
            return False
        if discription == []:
            return False
    except:
        return False
    sql_add = sql(headlines, discription, url, i)
    if sql_add[-1] == True:
        return (f"work with {url} is good, and we hav that {headlines}"
              f" and {discription}")
    else:
        return f"{sql_add}"


def test_past(url, headers):
    response = requests.get(url, headers=headers)
    tree = html.document_fromstring(response.text)
    headlines = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1/text()')
    discription = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')


def main():
    global i
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'Referer': 'http://porno365.lol/'
    }
    work = pats(f'http://porno365.lol/movie/{i}', headers)
    print(work)
    if work == False:
        return False
    #test_past(f'http://porno365.lol/movie/2', headers)
    i += 1


if __name__ == '__main__':
    i = 1
    kafizient = True
    while kafizient:
        mai = main()
        if mai == False:
            kafizient = False


