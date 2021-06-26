import requests
from lxml import html
from  sql_work import sql


def pats(url, headers, i):
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
            return [False, 'headline have nothing']
        if discription == []:
            return [False, 'discription have nothing']
    except:
        return [False, 'Connect to site error']
    sql_add = sql(headlines, discription, url, i)
    if sql_add[-1] == True:
        return (f"work with {url} is good, and we hav that {headlines}"
              f" and {discription}")
    else:
        return [False, f"{sql_add}"]


def test_past(url, headers):
    response = requests.get(url, headers=headers)
    tree = html.document_fromstring(response.text)
    headlines = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1/text()')
    discription = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')


if __name__ == '__main__':
    i = 1
    url = f'http://porno365.lol/movie/{i}'
    headers = {
        'User-Agent': 'Mozilla/4.9 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/92.0.4573.104 Safari/537.37',
        'Referer': 'http://porno365.lol/'}
    print(pats(url, headers, i))