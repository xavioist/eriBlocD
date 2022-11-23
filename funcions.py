def fancy_suma(x, y):
    """fancy_suma

    Args:
        x (int): un numero
        y (int): un altre numero

    Returns:
        int: suma formatada de x i y
    """
    return f"La suma de {x} i de {y} es {x+y}"


def foldl_str(x):
    if x == []:
        return ""
    return x.pop() + foldl_str(x)


def foldr_str(x):
    if x == []:
        return ""
    return x.pop(0) + foldr_str(x)
