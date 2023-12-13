#Дан список размера N. Найти минимальный из его локальных максимумов
#(локальный минимум — это элемент, который меньше любого из своих соседей).
N = int(input("Введите размер списка : "))
my_list = []
my2_list = []
K = 1
for i in range(N):
    number = int(input(f"Введите {K}-е число: "))
    K = K+1
    my_list.append(number)
print("Ваш список : " , my_list)

for g in range(len(my_list)):
    if g == 0:
        if my_list[g] < my_list[g+1]:
            my2_list.append(my_list[g])
    if g == len(my_list):
        if my_list[g] < my_list[g-1]:
            my2_list.append(my_list[g])
    if g != 0 and g != len(my_list):
        if my_list[g-1] > my_list[g] and my_list[g] < my_list[g+1]:
            my2_list.append(my_list[g])


print(min(my2_list))