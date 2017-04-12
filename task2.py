"""
Программа читает 2 массива. Первый массив — список строк Х. Второй массив — запросы У.
По каждому запросу У программа подсчитывает сколько раз эта строка встречается среди
элементов Х. По каждой У выводится количество в Х.
"""


def input_fill_list():
    """"Method to fill list by input"""
    l = []
    n = input('Please enter size of list:')
    try:
        n = int(n)
    except ValueError:
        input('Wrong input!\nPress enter to continue.')
        exit()
    else:
        for i in range(n):
            l.append(input('[%s] Enter value for X: ' % (i+1)))
        return l


def file_fill_list():
    """Method to fill list by file"""
    l = []
    path = input('Please enter full path to your file: ')  # You can use persons.txt at this folder to test this method
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line is not '':
                    l.append(line.replace('\n', ''))
    except FileNotFoundError:
        print('Wrong path!')
        input('Press enter to continue!')
        exit()
    return l


if __name__ == '__main__':
    # Constants
    event = {'1': file_fill_list, '2': input_fill_list}
    message = 'For fill {list_name} by file - press 1\nFor fill {list_name} by input - press 2\n-> '

    # Fill X and Y
    try:
        X = event[input(message.format(list_name='X'))]()
        Y = event[input(message.format(list_name='Y'))]()
    except KeyError:
        print('Wrong option!')
        input('Press enter to continue.')
        exit()
    # Create dict with keys - Y and values - how many times item from Y present in X
    result = {i: 0 for i in Y}

    # Find Y in X
    for i in X:
        if i in result.keys():
            result[i] += 1

    # Display result
    for k, v in result.items():
        print('%s - %s' % (k, v))
