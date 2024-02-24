#!/usr/bin/env python
# coding: utf-8

# ### Написать программу, которая запускается из консоли и считает сумму переданных в неё чисел; добавить произведение; по переданному параметру рассчитать либо сумму, либо произведение; оформить в доп модуль
# 

# In[57]:


def calculate_sum(numbers):
    return sum(numbers)

def calculate_multiplication(numbers):
    m = 1
    for num in numbers:
        m *= num
    return m

def main():
    print('Введите два числа через пробел и знак операции в последнюю очередь: ')
    numb = input().split()
    
    if not numb or len(numb) < 3:
        print("Нет данных или недостаточно данных")
        return

    try:
        numbers = [float(x) for x in numb[:-1]]
    except ValueError:
        print('Ошибка, введите числа, не символы или буквы')
        return

    operation = numb[-1]
    if operation == '+':
        result = calculate_sum(numbers)
        print(result)
    elif operation == '*':
        result = calculate_multiplication(numbers)
        print(result)
    else:
        print("Доступны только операции сложения и умножения: '+', '*'")

if __name__ == "__main__":
    main()

