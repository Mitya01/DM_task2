import time
from itertools import product


def boolean_build(b):
    """Возвращает булеан (все подмножества) заданного множества s с использованием 0 и 1."""
    # Генерируем все возможные комбинации 0 и 1 для каждого элемента в b
    binary_combinations = product([0, 1], repeat=len(b))

    # Создаем подмножества на основе бинарных комбинаций
    subsets = []
    for combination in binary_combinations:

        subset = list(element for element, included in zip(b, combination) if included == 1)
        if len(subset) == 0:
            subsets.append('∅')
        else:
            subsets.append(subset)

    return subsets

def boolean_answer(n, numbers):

    if n == 1:
        boolean = boolean_build(numbers)
        # Вывод каждого элемента булеана в отдельной строке
        return boolean

    if n > 1:
        boolean = boolean_build(numbers)
        beforebool  = boolean
        for i in range(n - 1):
            boolean = boolean_build(beforebool)
            beforebool = boolean
        return boolean

    if n < 1:
        print("Ошибка: n должно быть целым числом, большим 0")
        return None

def main():
    try:
        flag = input('Введите тип чисел, входящих в множество, в виде одной буквы Ц/В(целые или вещественные). ')
        numbers = []
        num_str = input("Введите числа, которые входят в множество, через пробел: ")  # Ввод чисел с клавиатуры
        # Преобразование строки в список чисел
        if flag == 'Ц':
            numbers = [int(x) for x in num_str.split()]
        if flag == 'В' or flag == 'B':
            numbers = [float(x) for x in num_str.split()]
        n = int(input("Введите порядок булеана (n): "))
        # Вывод булеана
        start_time = time.time()
        boolean = boolean_answer(n, numbers)
        print(f"\n Булеан {n}-ого порядка", sep = "")
        for el in boolean:
            print(el)
            # Если важно [] или {}
            # print(str(el).replace('[', '{').replace(']','}'))
        end_time = time.time()
        print("Время работы программы:", end_time - start_time, "с")
        print("Длина булеана:", len(boolean))

    except UnboundLocalError:
        print("Ошибка: Введите, пожалуйста, 1 букву (Ц или В)")
    except ValueError:
        print("Ошибка: элементы множества должны быть числами (int или float), n должно быть целым числом, большим 0 ")



if __name__ == "__main__":
    main()