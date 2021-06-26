from parsim import pats
from parsim import test_past
from sql_work import last_in_base
from random import randrange
import time

def random_headers(rand):
    if rand == True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Referer': 'http://porno365.lol/'
        }
    else:
        to5 = randrange(0, 50) / 10
        to10 = randrange(0, 9)
        to100 = randrange(0, 99)
        to1000 = randrange(0, 999)
        to10000 = randrange(0, 9999)
        headers = {
            'User-Agent': f'Mozilla/{to5} (Macintosh; Intel Mac OS X {to10}_{to10}) AppleWebKit/{to1000}.{to100} '
                          f'(KHTML, like Gecko) Chrome/{to100}.{to10}.{to10000}.{to1000} Safari/{to1000}.{to100}',
            'Referer': 'http://porno365.lol/'
        }
    return headers



def main():
    global i
    headers = random_headers(True)
    work = pats(f'http://porno365.lol/movie/{i}', headers, i)
    print(work)
    if work[0] == False:
        return False
    #test_past(f'http://porno365.lol/movie/2', headers)
    i += 1


if __name__ == '__main__':
    how_many_fals = 0
    plus = 1
    # 298
    TR = True
    while TR:
        if how_many_fals >= 3:
            print(f'сколько было ошибок {how_many_fals}')
            how_many_fals = 0
            plus += 1
            print(f'сколько плюсуем {plus}')
        try:
            i = last_in_base() + plus
            kafizient = True
            while kafizient:
                mai = main()
                if mai == False:
                    kafizient = False
                    print(mai)
                    int('q')
                else:
                    plus = 1
                    how_many_fals = 0
        except:
            how_many_fals += 1
            #print(f'time to sleep')
            time.sleep(30)

