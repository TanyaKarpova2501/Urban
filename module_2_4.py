number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum_ = 0
for a in number:
    print(a)
    prime = [a for a in range(2, 16, 2)]
    print(prime)
    not_prime = [a for a in range(3, 16, 2)]
    print(not_prime)