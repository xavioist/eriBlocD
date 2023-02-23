def func2(x):
    if x == []:
        return 0
    return x.pop() + func2(x)
