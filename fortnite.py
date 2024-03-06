for i in range(100, 1000): #Берем все 3 значные числа
    if (str(i)[0] != str(i)[1]) and (str(i)[2] != str(i)[1]) and (str(i)[0] != str(i)[2]):
        print(i,end = ' ')
