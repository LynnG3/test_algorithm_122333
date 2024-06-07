"""Программа выводит n первых элементов последовательности 122333444455555…
(число повторяется столько раз, чему оно равно). """


def generate_first_elements(n):
    """Принимает на вход число n.
    Возвращает n первых элементов последовательности или ошибку,
    если введенное число вне корректного диапазона . """
    # Проверяет, что n больше 0
    if n < 1:
        raise ValueError("Число n должно быть больше 0")
    # Проверяет, что n не слишком велико
    if n > 10000000:
        raise ValueError("Число n слишком велико")
    # Генерирует последовательность
    sequence = []
    current_number = 1
    while len(sequence) < n:
        sequence.extend([current_number] * current_number)
        current_number += 1
    return sequence[:n]


def main():
    try:
        n = int(input("Введите число n: "))
        result = generate_first_elements(n)
        print("".join(map(str, result)))
    except ValueError as e:
        # Обрабатывает ошибку ввода нецелого числа или нечислового значения
        print("Ошибка:", e)
    except Exception as e:
        print("Произошла неожиданная ошибка:", e)


if __name__ == "__main__":
    main()
