# Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица
# Лекарственные Средства должна содержать следующую информацию: Код, Название
# препарата, Применение, Количество, Цена, Страна-производитель.

import sqlite3 as sp

with sp.connect('base.db') as conn:
    cur = conn.cursor()

    cur.execute(
        """CREATE TABLE IF NOT EXISTS medications(
        id INTEGER PRIMARY KEY,
        name VARCHAR(100),
        country VARCHAR(100),
        info VARCHAR(100),
        count INTEGER,
        pay INTEGER)
    """)

with conn:
    cur = conn.cursor()
    cur.execute("DELETE FROM medications")
    cur.executemany("INSERT INTO medications VAlUES(NULL,?,?,?,?,?)", [
        ('супрастин','Germany','сделано с использованием чего-то там',25,255),
        ('миромистин','RUSSIA','сделано с использованием чего-то там',15,140),
        ('аквамарис','Germany','сделано с использованием чего-то там',23,600),
        ('альбуцин','Ital','сделано с использованием чего-то там',42,255),
        ('зовиракс','RUSSIA','сделано с использованием чего-то там',35,255),
        ('спирт муравьиный','RUSSIA','сделано с использованием чего-то там',125,60),
        ('тренбалон','France','сделано с использованием чего-то там',87,35),
        ('отипакс','Kanada','сделано с использованием чего-то там',55,345),
        ('подгузники','Korea','сделано с использованием чего-то там',27,999),
        ('подгузники для взрослых','Korea','сделано с использованием чего-то там',5,1199),
    ])

with conn:
    cur = conn.cursor()
    print(*cur.execute('SELECT * FROM medications WHERE name = "тренбалон" ORDER BY id DESC').fetchall(), sep='\n', end='\n\n')
    print(*cur.execute('SELECT * FROM medications WHERE pay >= 300').fetchall(), sep='\n', end='\n\n')
    print(*cur.execute('SELECT name FROM medications').fetchall(), sep='\n', end='\n\n')

with conn:
    cur = conn.cursor()
    cur.execute('DELETE FROM medications WHERE name = ?', ('подгузники',))
    cur.execute('DELETE FROM medications WHERE count >= 52')
    cur.execute('DELETE FROM medications WHERE pay <= 40')


with conn:
    cur = conn.cursor()
    cur.execute('UPDATE medications SET pay = 200 WHERE pay = 140')
    cur.execute('UPDATE medications SET country = "Germany" WHERE country = "BeloRussia"')
    cur.execute('UPDATE medications SET info = "сделано без использованием чего-то там" WHERE info = "сделано с использованием чего-то там"')
