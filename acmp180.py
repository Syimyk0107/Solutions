def find_smallest_q(n,k):
    
    if n>k and k == 1:
        return 1  # 1 - единственное число, произведение цифр которого равно 1

    factors = []

    # Разложение числа N на множители от 9 до 2
    for d in range(9, 1, -1):
        while k % d == 0:
            factors.append(d)
            k //= d

    # Если после разложения осталось число больше 1, значит, оно содержит простые множители больше 9 → ответа нет
    if k > 1:
        return -1

    # Сортируем множители, чтобы получить наименьшее число
    return int("".join(map(str, sorted(factors))))
    
# Ввод числа N
n, k = map(int,input().split())


result = find_smallest_q(n,k)

if n>k and result>=1 and result<=n:
    print("YES")
elif n==k or result==-1 or n<k and result<1 or n<k and result>1 or n>k and result>1 and result>n:
    print("NO")

# Вывод результата
# print(result)

