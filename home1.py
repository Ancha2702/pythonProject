"""Задание 1.
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False
в противном случае. Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""
import subprocess

def check_output(cmd, txt):
    out = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if out.returncode == 0:
        if txt in out.stdout:
            return True
        else:
            return False
    else:
        return f'error command: {cmd}'


result = check_output("cd", "m")
print(result)
