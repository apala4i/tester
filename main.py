from tkinter import filedialog
import subprocess


def test_count(sign):
    while True:
        try:
            count = int(input('Введите количество {c} тестов\n'.format(
                c='позитивных' if sign else 'негативных')))
            return count
        except ValueError:
            print("Неккоректное количество тестов, попробуйте ещё раз")


def path():
    return filedialog.askdirectory().replace('\\', '/')


def test_creator(sign, cur_test, change_mod=0):
    test_number = cur_test
    if change_mod:
        print("Вы находитесь в режиме измненения.\n")
    print('Введите значения для {} {c} теста'.format(test_number,
                                                     c='положительного' if sign else 'отрицательного'))
    test = input()
    if not change_mod:
        if 'change'.lower() in test:
            if len(test.split()) == 2:
                return [int(test.split()[1]), 2]
            else:
                return [cur_test - 1, 1]
    open(full_path + '/' + test_name(test_number, sign) + '_in.txt', 'w').write(test)
    cmd = full_path + '/a.exe < ' + full_path + test_name(test_number, sign) + '_in.txt'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0]
    result = result.decode('cp1251')
    print(f"Результат:\n{result}")
    open(full_path + test_name(test_number, sign) + '_out.txt', 'w').write(result)
    return [0, 0]


def test_name(number, test):
    if test:
        return '/pos_0{}'.format(number)
    else:
        return '/neg_0{}'.format(number)


print('Добро пожаловать в создатель тестов.\n1 - выбрать папку с програмой')
while True:
    try:
        flag = int(input())
        if flag == 1 or flag == 228:
            break
        else:
            print("Некорректный ввод, попробуйте ещё раз\n")
    except ValueError:
        print("Некорректный ввод, попробуйте ещё раз\n")
full_path = path() if flag == 1 else 'C:/test'
if flag == 228:
    print("Стандартный путь установлен")
choice = 1
while choice != 0:
    while True:
        try:
            choice = int(input('1 - Записать позитивные тесты\n2 - записать '
                               'негативные тесты\n3 - сменить путь\n4 - инфо\n'))
            break
        except ValueError:
            print("Зачем ты ломаешь программу?\nНекорректный ввод, попробуй ещё раз\n")
    if choice == 1 or choice == 2:
        decision = 1 if choice == 1 else 0
        count = test_count(decision)
        i = 1
        while i <= count:
            check = test_creator(decision, i)
            if check[1] == 2:
                test_creator(decision, check[0], change_mod=1)
                print("\nтест изменён, ввод тестов в прежнем порядке возобновлён\n\n")
            elif check[1] == 1:
                i = check[0]
            else:
                i += 1

    elif choice == 3:
        full_path = path()
    elif choice == 4:
        print('Данная программа позволяет быстро создать позитивные\n'
              'и негативные тесты. Тестовые файла будут автоматически'
              ' созданы и\nназваны как надо. Для корректной работы программы'
              ' исполняемый файл должен называется a.exe.\n       Пиписька.')
    else:
        print("Такого пункта нет, попробуй ещё раз\n")
