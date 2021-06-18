import datetime
from datetime import date
from  parsim import pats2


def main(jar, month, day):
    i = 0
    x = datetime.datetime.now()
    x = str(x)
    x = x[0:10]
    x = x.split('-')
    x[1] = str(int(x[1]))
    while [str(jar), str(month), str(day)] != x:
        #print([str(jar), str(month), str(day)], x)
        try:
            d = date(jar, month, day)
            day += 1
            d = str(d)
            d = d.split('-')
            d = [d[0], d[1], d[2]]
            #print(d)
            #print(f'https://lenta.ru/{d[0]}/{d[1]}/{d[2]}/')
            i += 1
            print(i)
            pats2(f'https://lenta.ru/{d[0]}/{d[1]}/{d[2]}/')
        except:
            month += 1
            if month == 13:
                month = 1
                jar += 1
            day = 1


if __name__ == '__main__':
    main(2006, 7, 3)
