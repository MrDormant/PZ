#Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
#нечетные числа в порядке возрастания их индексов, а также их количество K.
K = 1
my_list=[]
for i in range(10):
    number = int(input(f"Введите {K}-е число: "))
    K=K+1
    my_list.append(number)
print("Ваш список : ",my_list)

result = list(filter(lambda x: (x%2 != 0) , my_list))

print("Нечетные числа в порядке возрастания их индексов : ",result,
      "\nТакже их количество :", len(result) )
