import requests
from lxml import html
from  sql_work import sql


def pats(url, headers, i):
    # give url, pc information and video number
    #
    # //*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/article/div[1]/div/h1/span
    # //*[@id="app"]/div/div[2]/main/div/div/div/div[1]/div/div[2]/article/div[1]/div/h1/span
    #
    # headline, discription, url, somphing
    # headline
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1/text()
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[2]/h1
    # discription
    # /html/body/div[6]/div[1]/div[1]/div[1]/div[3]/div[9]/text()
    #
    # print with what url work
    print(f'work with url:{url}')
    try:
        # download html size
        response = requests.get(url, headers=headers)
        # convert html to python variable
        tree = html.document_fromstring(response.text)
        # give from html size headline
        headlines = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1/text()')
        # give from html size description
        description = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')
        # if we cant get headline return error
        if headlines == []:
            return [False, 'headline have nothing']
        # if we cant get description return error
        if description == []:
            return [False, 'discription have nothing']
    except:
        # if we cant connect to server return error
        return [False, 'Connect to site error']
    # add in sql table
    sql_add = sql(headlines, description, url, i)
    # if can add to sql table return good status
    if sql_add[-1] == True:
        return (f"work with {url} is good, and we hav that {headlines}"
              f" and {description}")
    # if cant add to table return false
    else:
        return [False, f"{sql_add}"]


def test_past(url, headers):
    # test to connect
    response = requests.get(url, headers=headers)
    tree = html.document_fromstring(response.text)
    headlines = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[2]/h1/text()')
    description = tree.xpath(f'//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[9]/text()')
    return [headlines, description]


if __name__ == '__main__':
    i = 1
    url = f'http://porno365.lol/movie/{i}'
    headers = {
        'User-Agent': 'Mozilla/4.9 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/92.0.4573.104 Safari/537.37',
        'Referer': 'http://porno365.lol/'}
    print(test_past(url, headers, i))