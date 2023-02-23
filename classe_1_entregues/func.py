def func(x):
    if x == []:
        return 0
    return x.pop() + func(x)
