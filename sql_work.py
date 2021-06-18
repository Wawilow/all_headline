import sqlite3


def sql(sag, data, somphing):
    all_users = []
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    result = cur.execute("""SELECT * FROM lenta_ru""").fetchall()
    for elem in result:
        all_users.append(elem)
    # print(all_users)
    param = (str(sag[0]), str(data[0]), str(somphing))
    con.execute("""insert into lenta_ru values (?, ?, ?)""", param)
    con.commit()
    con.close()


#sql('пример заголовка', '0000 0 0', 'url')