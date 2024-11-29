from random import randint

r = (randint(3, 20))

result = 0

for i in range(1, 51):
    for j in range(1, 51):
        if i != j and (i + j) % r == 0 and (i + j) != r:
            result = i + j
            break
        if result:
            break

print(f"Пара чисел, сумма которых кратна {r}: {result}")