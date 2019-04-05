def get_fibonacci(num):
    return 0 if num == 0 else 1 if num == 1 else get_fibonacci(num - 2) + get_fibonacci(num - 1)


int_num = 10

print('Bai 3: In ra %d so fibonacci dau tien: ' % int_num)
for i in range(0, int_num):
    print(get_fibonacci(i), end=', ')
