import requests
from lxml import html
from  sql_work import sql


def pats(url):
    global i
    # headline, discription, url, somphing
    # headline
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1/text()
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1
    # discription
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[3]/div[9]/text()
    #
    print('work')
    i += 1
    request = requests.get(url)
    tree = html.document_fromstring(request.text)
    headline = tree.xpath(f'/html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1/text()')
    discription = tree.xpath(f'/html/body/div[6]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')
    print(i, headline, discription)
    print(sql(headline, discription, url, ''))


def test_past(url):
    # //*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1
    global i
    request = requests.get(url)
    tree = html.document_fromstring(request.text)
    headline = None
    print(tree.xpath('/html/body/div[4]/section[2]/div[2]/div/div[1]/section/div[1]/a/h3/text()'))
    print(headline)

def main():
    #test_past(f'http://porno365.lol/movie/{i}')
    test_past(f'https://vk.com/interestingstatistic')


if __name__ == '__main__':
    i = 2
    main()