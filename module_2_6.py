from random import randint
r = (randint(3, 20))

def get_password(r):
    password = ''
    for i in range(1, r):
        for j in range(2, r):
            if j <= i:
                continue
            if r % (i + j) == 0:
                password += str(i) + str(j)

    return password

result = get_password(r)
print(r)
print('Пароль:', result)
