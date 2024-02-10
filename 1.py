def gen_func(n):
    for i in range(1,n+1):
        yield i

numbers=gen_func(5)

next(numbers)
result=next(numbers)
print(result)