def get_fibonacci(num):
    '''
    Get the value of the fibonacci
    :param num: The number convert to fibonacci
    :return: The fibonacci number
    '''
    return 0 if num == 0 else 1 if num == 1 else get_fibonacci(num - 2) + get_fibonacci(num - 1)
