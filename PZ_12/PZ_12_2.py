"""
2. Составить генератор (yield), который преобразует все буквенные символы в
строчные
"""


def lowergen(text):
    for i in text:
        yield i.lower()


text = str(input("Введите текст: "))
lasttext = ''.join(i for i in lowergen(text))
print(lasttext)
