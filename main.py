from parsim import pats
from parsim import test_past
from sql_work import last_in_base
from random import randrange
import time
from icecream import ic


# i use better print, which print more information
ic.configureOutput(includeContext=True)
# but in program i write just print
print = ic


def random_headers(rand):
    # if you give True in function then generated random numbers in the headers
    # if you give False, then random is off
    if rand == False:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Referer': 'http://porno365.lol/'
        }
    else:
        # make a lot of random
        to5 = randrange(0, 50) / 10
        to10 = randrange(0, 9)
        to100 = randrange(0, 99)
        to1000 = randrange(0, 999)
        to10000 = randrange(0, 9999)
        # make dictionary with random
        headers = {
            'User-Agent': f'Mozilla/{to5} (Macintosh; Intel Mac OS X {to10}_{to10}) AppleWebKit/{to1000}.{to100} '
                          f'(KHTML, like Gecko) Chrome/{to100}.{to10}.{to10000}.{to1000} Safari/{to1000}.{to100}',
            'Referer': 'http://porno365.lol/'
        }
    # always return header, if true with random, if false without random
    return headers



def main():
    global i
    # make a random browser information
    headers = random_headers(True)
    # calling the pats function (in parsim file), he print with what url we work
    # if all be fine, he back a str, if we have problem he back a list, first elem is False
    # and second is how error we have
    work = pats(f'http://porno365.lol/movie/{i}', headers, i)
    print(work)
    # print what back pats function
    if work[0] == False:
        # if it is list, and list hav first elem false, we return false
        return False
    #
    # here i tested connect to site
    #
    #test_past(f'http://porno365.lol/movie/2', headers)
    #
    # i plus a video number always, because something video deleted
    i += 1


if __name__ == '__main__':
    # make a flag, how many fails we hav
    how_many_fals = 0
    # how many plus we make
    plus = 1
    # make infinite loop
    TR = True
    while TR:
        # if fails flag is more 3
        # then we try to connect error three times
        if how_many_fals >= 3:
            # write hov many fails we hav
            print(f'сколько было ошибок {how_many_fals}')
            # if we have 3 error, we connect to other url
            # and because this video dont downloaded, we try to downloaded next video
            # vor then whe make "plus" for one
            # because we try to downloaded new video, then we havent fails with video
            # and fails = 0
            how_many_fals = 0
            plus += 1
            # write how many we plus to i
            print(f'сколько плюсуем {plus}')
        try:
            # configure i, we search a last kaf in sql table and plus plus
            i = last_in_base() + plus
            kafizient = True
            # make a new infinite loop
            while kafizient:
                mai = main()
                # calling main function
                # if he back return false we stop loop
                if mai == False:
                    kafizient = False
                    print(mai)
                    # print fail
                    int('q')
                    # make error, to call except, eah this bad, but work cool
                else:
                    # if all be good, we plus one, because last in table is new record
                    plus = 1
                    how_many_fals = 0
        except:
            # if error, then plus fails
            how_many_fals += 1
            #
            # print(f'time to sleep')
            #
            # sleep some time to you cann see
            time.sleep(0.1)
            if plus >= 50:
                # if we have 50 fails video, then size block us
                # and all video, then we try to connect dosent deleted
                # then we try to connect him again, but after we ned some time wait to size removed block
                plus = 0
                # but is size admin deleted more 50 videos, then program broke down
                time.sleep(720)

