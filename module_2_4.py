number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14, 15]
n = int(input("Введите от 1 до 15 "))
p = 2
for p in range(len(number)):
    for i in range(2, p):
        if p % i == 0:
            break
    else:
        print(p)
print('Done')