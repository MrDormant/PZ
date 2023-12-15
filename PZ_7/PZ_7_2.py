Simv = str(input("введите вашу строку "))
k = ""
for i in range(-1,-10,-1):
    if Simv[i] == ".":
        break
    print(Simv[i])
    k = k + str(Simv[i])
print('Вид разширения : ', k[::-1])
