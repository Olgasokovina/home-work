# number - загаданное число
# predict_number - предпологаемое число
# N0 .. N- Диапазон чисел из которого угадываем, где N0 - начало диапазона, N - конец диапазона
# позволяет в любой момент изменить диапазон без существенного изменения кода
# count- число попыток

from statistics import mean


def guess_number(N0=1, N=100):
    """
    Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать
    Необходимо добиться минимального количества попыток
    """
    
    import numpy as np 
    
    number = np.random.randint(N0, N+1)
    #print('загаданное число', number)
    predict_number = (N0 + N) // 2
    #print('предполагаемое число', predict_number)
    count = 1
    N0 = N0 - 1
    N = N + 1

    while True:
        if predict_number == number:       
            break
        
        count += 1
        if predict_number < number:
            N0 = predict_number 
            predict_number = (N0 + N) // 2
            #print('предполагаемое число', predict_number, "диапазон", N0, N)
            
        else:
            N = predict_number
            predict_number = (N0 + N) // 2
            #print('предполагаемое число', predict_number,"диапазон", N0, N)
        
                
    #print (f'Число угадали за {count} попыток')
    return count

# Проведем тестирование алгоритма: запустим алгоритм 10000 раз и найдем максимальное комичество попыток. 

a = []

for i in range(10000):    
   a.append(guess_number())

z = max(a)
c = mean(a)
print('максимальное число попыток', z)
print('среднее число попыток', c)
    