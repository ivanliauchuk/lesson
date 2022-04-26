def sayGenerator():
    a = 'like'

    for i in range(5):
        yield i
        print(a)


a = sayGenerator()

print(next(a))
print(next(a))
print(next(a))
print(next(a))

 