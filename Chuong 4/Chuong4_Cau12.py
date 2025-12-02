def oscillate(start, end):
    for i in range(start, end + 1):
        yield i
        yield -i


# Test
for n in oscillate(-3, 4):
    print(n, end=' ')
