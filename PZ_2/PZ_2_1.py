# Дано трехзначное число.Вывести число,полученное при прочтении числа справа налево.
while True:
    try:
        count = int(input("введите трехзначное число : "))
        break
    except ValueError:
        print('вы ввели не число!')
Ferstnum = count // 100
Thirdnum = count % 10
secondnum = count // 10 % 10
Lnumber=Thirdnum*100+secondnum*10+Ferstnum
print("вывод: ",Lnumber)

