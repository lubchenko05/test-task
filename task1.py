import os


"""
Задание 1:
Написать программу с использованием декораторов которая принимает целое число и затем
несколько строк со следующей структурой: имя фамилия, возраст, пол. И возвращает список с
обращениями (Г-н, Г-жа) отсортированный по возрасту. Если возраст одинаковый —
сохраняется порядок ввода.
"""


class Person:
    """Class model for our person"""
    def __init__(self, init_str):
        data = init_str.split()
        self.first_name = data[0]
        self.last_name = data[1]
        if data[2] == 'М':
            self.gender = 'Г-н'
        elif data[2] == 'Ж':
            self.gender = 'Г-жа'
        else:
            self.gender = '<Unknown gender>'
        self.age = int(data[3])

    def __str__(self):
        return self.gender + ' ' + self.first_name + ' ' + self.last_name


def clear():
    """ Method that clear console """
    os.system('cls') if os.name == 'nt' else os.system('clear')


def output_persons(f):
    """Method that display persons"""
    def wrapper():
        clear()
        result = f()
        if len(result) > 0:
            result.sort(key=lambda _person: _person.age)
            print('List of users:')
            for i in result:
                print(str(i))
        else:
            print('No persons detected!')
        input('Press enter to continue.')
    return wrapper


@output_persons
def input_file():
    """Input persons by file"""
    person_list = []
    path = input('Please enter full path to your file:')  # You can use persons.txt at this folder to test this method
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if line is not '':
                    person_list.append(Person(line.replace('\n', '')))
    except FileNotFoundError:
        print('Wrong path!')
        input('Press enter to continue!')
    return person_list


@output_persons
def input_line():
    """Input persons by console"""
    person_list = []
    count = input('Please enter count of users that you want to add: ')
    try:
        count = int(count)
        if count <= 0:
            raise ValueError
    except ValueError:
        print('Input is not valid! Please enter integer!')
        input('Press enter to continue.')
        clear()

    for i in range(count):
        try:
            person = Person(input('[%s] Enter user init string, for example "Иван Петров М 34": ' % (i+1)))
        except IndexError:
            print('Wrong input!')
        else:
            person_list.append(person)
    return person_list

if __name__ == '__main__':
    while True:
        # Constants
        event = {'0': exit, '1': input_line, '2': input_file}

        # Display menu
        clear()
        response = input('Hello!\n'
                         'If you want to input users by console please press "1"\n'
                         'Or if you want to include text file please press "2"\n'
                         'To exit please press "0"\n'
                         '-> ')
        clear()

        # Action controller
        try:
            event[response]()
        except KeyError:
            print('Wrong input, please try again!')
