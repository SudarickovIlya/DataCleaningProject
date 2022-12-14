import numpy as np

number = np.random.randint(1, 101) # Загадываем число
count = 0

while True:
    count+=1
    predict_number = int(input('Введите число'))
    
    if predict_number > number:
        print ('Слишком большое число')
    elif predict_number < number:
        print ("Слишком маленькое число")
    else:
        print(f"Вы угадали число. Это - {number}. Количество попыток - {count}.")
        break 
