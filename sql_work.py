import sqlite3


def sql(headline, discription, url, somphing):
    try:
        con = sqlite3.connect("all_headlins.db")
    except:
        return 'connect to base error'
    cur = con.cursor()
    #подключаем бузу данных, если не подключилась то возвращает ошибку
    #задаем курсор который будет бежать по базе данных
    try:
        result = cur.execute("""SELECT * FROM base_prn""").fetchall()
        all_users = [elem for elem in result]
    except:
        return 'select from base error'
    #бежим по базе данных
    #если крашнулось выдает ошибку
    try:
        param = (str(headline), str(discription), str(url), str(somphing))
        con.execute("""insert into base_prn values (?, ?, ?, ?)""", param)
    except:
        return 'insert to base error'
    # добовляем в базу данных заданные переменные
    # если крашнулось возращаем ошибку
    con.commit()
    con.close()
    return [all_users, True]


if __name__ == '__main__':
    pass
    #sql('пример заголовка', 'пример описания', 'ссылка на видео', 'что то еще')
    # what, what?