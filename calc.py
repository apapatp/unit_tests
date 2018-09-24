def add(x, y):
    """ Add function """
    return x + y

def subtract(x, y):
    """ Add function """
    return x - y

def multiply(x, y):
    """ Add function """
    return x * y

def divide(x, y):
    """ Add function """
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y