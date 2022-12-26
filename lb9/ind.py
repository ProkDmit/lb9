#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    students = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break
        elif command == 'add':
            name = input("Ф.И.О.? ")
            group = input("Номер группы? ")
            ac_per = str(input('Успеваемость: '))
            student = {
                'name': name,
                'group': group,
                'ac_per': ac_per,
            }
            students.append(student)
            if len(students) > 1:
                students.sort(key=lambda item: item.get('group')[::-1])
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "№",
                    "Ф.И.О.",
                    "Группа",
                    "Успеваемость"
                )
            )
            print(line)
            for idx, student in enumerate(students, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        student.get('name', ''),
                        student.get('group', ''),
                        student.get('ac_per', 0)
                    )
                )
            print(line)
        elif command.startswith('select'):
            count = 0
            for student in students:
                ac_per = list(map(int, student.get('ac_per', '').split()))
                if sum(ac_per) / max(len(ac_per), 1) >= 4.0:
                    print(
                        '{:>4} {}'.format('*', student.get('name', '')),
                        '{:>1} {}'.format('группа №', student.get('group', ''))
                    )
                    count += 1
            if count == 0:
                print("Студенты с баллом 4.0 и выше не найдены.")
        elif command == 'help':
            print("add - добавить студента")
            print("list - вывести список студентов")
            print("select - вывести студентов с баллом 4.0 или выше")
            print("help - отобразить справку")
            print("exit - завершить работу с программой")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
