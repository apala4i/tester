from tkinter import filedialog
import subprocess


def test_count(sign):
    while True:
        try:
            count = int(input('Input count of {c} tests\n'.format(
                c='positive' if sign else 'negative')))
            return count
        except ValueError:
            print("Incorrect input, try again\n")


def path():
    return filedialog.askdirectory().replace('\\', '/')


def test_creator(sign, cur_test, change_mod=0):
    test_number = cur_test
    if change_mod:
        print("Switched to edit mod.\n")
    print('Enter values for {} {c} test'.format(test_number,
                                                     c='positive' if sign else 'negative'))
    test = input()
    if not change_mod:
        if 'change'.lower() in test:
            if len(test.split()) == 2:
                return [int(test.split()[1]), 2]
            else:
                return [cur_test - 1, 1]
    open(full_path + '/func_tests/' + test_name(test_number, sign) + '_in.txt', 'w').write(test)
    cmd = full_path + '/a.exe < ' + full_path + '/func_tests/' + test_name(test_number, sign) + '_in.txt'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    result = p.communicate()[0]
    result = result.decode('cp1251')
    print(f"Result:\n{result}")
    open(full_path + '/func_tests/' + test_name(test_number, sign) + '_out.txt', 'w').write(result)
    return [0, 0]


def test_name(number, test):
    if test:
        return '/pos_0{}'.format(number)
    else:
        return '/neg_0{}'.format(number)


print('Welcome to the test creator.\n1 - chose folder with program')
while True:
    try:
        flag = int(input())
        if flag == 1 or flag == 228:
            break
        else:
            print("Incorrect input, try again\n")
    except ValueError:
        print("Incorrect input, try again\n")
full_path = path() if flag == 1 else 'C:/test'
if flag == 228:
    print("standard path was set")
choice = 1
while choice != 0:
    while True:
        try:
            choice = int(input('1 - Write positive tests\n2 - Write '
                               'negative tests\n3 - change path\n4 - make dir func_tests\n5 - info\n'))
            break
        except ValueError:
            print("Incorrect input, try again\n")
    if choice == 1 or choice == 2:
        decision = 1 if choice == 1 else 0
        count = test_count(decision)
        i = 1
        while i <= count:
            check = test_creator(decision, i)
            if check[1] == 2:
                test_creator(decision, check[0], change_mod=1)
                print("\ntest was changed, the input order has been resumed\n\n")
            elif check[1] == 1:
                i = check[0]
            else:
                i += 1

    elif choice == 3:
        full_path = path()
    elif choice == 4:
        subprocess.run(f'cd {full_path} && mkdir func_tests', shell=True)
        print("folder was created.\n")
    elif choice == 5:
        print('len\' perevodit\' bilo pizdez')
    else:
        print("There are no such variant, try again\n")
