# Проверка на простое число (при ответе True)

def prime(n):
    res = []
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            res.append(d)
            k = n // d
            if k != d:
                res.append(k)
        d += 1
    return not res

print(prime(11))
