def square_generator(limit):
    n = 0
    while n < limit:
        yield n ** 2
        n += 1
        limit=5
        squares= square_generator(limit)
        for square in squares:
            print(square)
