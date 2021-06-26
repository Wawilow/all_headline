from parsim import pats
from parsim import test_past
from sql_work import last_in_base

def main():
    global i
    headers = {
        'User-Agent': 'Mozilla/4.9 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/92.0.4573.104 Safari/537.37',
        'Referer': 'http://porno365.lol/'
    }
    work = pats(f'http://porno365.lol/movie/{i}', headers, i)
    print(work)
    if work[0] == False:
        return False
    #test_past(f'http://porno365.lol/movie/2', headers)
    i += 1


if __name__ == '__main__':
    i = last_in_base() + 1
    kafizient = True
    while kafizient:
        mai = main()
        if mai == False:
            kafizient = False