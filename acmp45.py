def find_smallest_q(n):
    if n==0:
        return 10
    elif n == 1:
        return 1  # 1 - единственное число, произведение цифр которого равно 1

    factors = []

    # Разложение числа N на множители от 9 до 2
    for d in range(9, 1, -1):
        while n % d == 0:
            factors.append(d)
            n //= d

    # Если после разложения осталось число больше 1, значит, оно содержит простые множители больше 9 → ответа нет
    if n > 1:
        return -1

    # Сортируем множители, чтобы получить наименьшее число
    return int("".join(map(str, sorted(factors))))

# Ввод числа N
n = int(input())

# Вычисление результата
result = find_smallest_q(n)

# Вывод результата
print(result)

