from tkinter import filedialog
import subprocess


def path():
    return filedialog.askdirectory().replace('\\', '/')


def test_name(number, test):
    if test:
        return '/pos_0{}'.format(number)
    else:
        return '/neg_0{}'.format(number)


print('Добро пожаловать в создатель тестов.\n1 - выбрать папку с програмой')
while True:
    flag = int(input())
    if flag == 1:
        break
full_path = path()
choice = 1
while choice != 0:
    choice = int(input('1 - Записать позитивные тесты\n2 - записать '
                       'негативные тесты\n3 - сменить путь\n4 - инфо\n'))
    if choice == 1:
        count = int(input('Введите количество позитивных тестов\n'))
        for i in range(count):
            print('Введите значения для {} положительного теста'.format(i + 1))
            open(full_path+'/'+test_name(i+1, 1) + '_in.txt', 'w').write(input())
            cmd = full_path + '/a.exe < ' + full_path + test_name(i + 1, 1) + '_in.txt'
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            result = p.communicate()[0]
            result = result.decode('cp1251')
            open(full_path+test_name(i + 1, 1)+'_out.txt', 'w').write(result)
    if choice == 2:
        count = int(input('Введите количество негативных тестов\n'))
        for i in range(count):
            print('Введите значения для {} негативного теста'.format(i + 1))
            open(full_path+'/'+test_name(i+1, 0) + '_in.txt', 'w').write(input())
            cmd = full_path + '/a.exe < ' + full_path + test_name(i + 1, 0) + '_in.txt'
            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
            result = p.communicate()[0]
            result = result.decode('cp1251')
            open(full_path+test_name(i + 1, 0)+'_out.txt', 'w').write(result)
    if choice == 3:
        full_path = path()
    if choice == 4:
        print('Данная программа позволяет быстро создать позитивные\n'
              'и негативные тесты. Тестовые файла будут автоматически'
              ' созданы и\nназваны как надо. Для корректной работы программы'
              ' исполняемый файл должен называется a.exe.\n       Пиписька.')
