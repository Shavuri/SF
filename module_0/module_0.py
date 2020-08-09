#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

number = np.random.randint(1, 101)
list = [i for i in range(1, 101)]  # назначаем массив, в котором будем искать число
max = 101


def game_core_v2(number):
    start = 0  # начальный индекс
    end = max - 1  # конечный индекс
    count = 0
    while start <= end:  # начинаем искать диапазон загаданного числа
        count += 1  # задаем алгоритм счетчика
        predict = (start + end) // 2  # делим массив на две почти равные части
        if number < list[predict]:  # если загаданное число  находится ниже индекса середины
            end = predict - 1  # то верхняя граница сдвигается на середину
        elif number > list[predict]:    # если загаданное число находится выше индекса середины
            start = predict + 1  # то нижняя граница начинается с индекса середины
        else:
            return (count)


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v2)


# In[ ]:




