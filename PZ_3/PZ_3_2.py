# Даны три переменные вещественного типа: A, B, C. Если их значения упорядочены
# по возрастанию, то удвоить их; в противном случае заменить значение каждой
# переменной на противоположное. Вывести новые значения переменных A, B, C.

a, b, c = input("Введите первое число: "), input("Введите второе число: "),input("Введите третье число: ")
while type(a) != float: # обработка исключений
 try:
    a = float(a)
 except ValueError:
    print("Неправильно ввели!")
    a = input("Введите первое число: ")
while type(b) != float: # обработка исключений
 try:
  b = float(b)
 except ValueError:
    print("Неправильно ввели!")
    b = input("Введите второе число: ")
while type(c) != float: # обработка исключений
 try:
     c = float(c)
 except ValueError:
     print("Неправильно ввели!")
     c = input("Введите третье число: ")
if (a<b<c) :
 a *= 2;b *= 2;c *= 2;
 print(a,b,c)
else:
 a = -a; b = -b; c = -c;
 print(a, b, c)