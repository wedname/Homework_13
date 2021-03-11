"""
Задание:
1) В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют
средний балл за национальной шкалой более «4».
"""
path_1 = "Task_1/file.txt"


def average_score(filename):
    students = []
    grades = []
    sum_grades = []
    student = []
    with open(filename, "r", encoding="utf8") as open_file:
        for line in open_file:
            for i in line:
                if i.isdigit():
                    sum_grades.append(int(i))
                    grades.append(i)
                elif i.isalpha():
                    student.append(i)
            if (sum(sum_grades)/len(sum_grades)) < 4:
                students.append({"student": "".join(student), "grades": grades})
            else:
                students.append({"student": ("".join(student)).lower(), "grades": grades})
            sum_grades = []
            grades = []
            student = []
        print(students)

    with open(filename, "w", encoding="utf8") as write_file:
        for i in range(len(students)):
            write_file.write(f"{students[i]['student']} - {', '.join(students[i]['grades'])}\n")


average_score(path_1)

"""
2) Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при этом из каждой строки должно быть
удалено только четное количество таких слов.
"""
path_2 = "Task_2/file.txt"


def delete_small_words(filename):
    lines = []
    with open(filename, "r", encoding="utf8") as open_file:
        for line in open_file:
            current_line = line.split()
            count = 0
            for word in current_line:
                if 3 <= len(word) <= 5:
                    count += 1

            if count % 2 == 0:
                for idx, word in enumerate(current_line):
                    if 3 <= len(word) <= 5:
                        current_line.pop(idx)
                lines.append(current_line)

            if count % 2 != 0:
                for idx, word in enumerate(current_line):
                    if 3 <= len(word) <= 5 and count != 1:
                        current_line.pop(idx)
                        count -= 1
                lines.append(current_line)

    with open(filename, "w", encoding="utf8") as write_file:
        for i in range(len(lines)):
            write_file.write(f"{' '.join(x for x in lines[i])}\n")


delete_small_words(path_2)

"""
3) Из текста программы выбрать все числа (целые и вещественные) и записать их в файл g в виде: число 1 – номер строки,
число 2 – номер строки и так далее.
В качестве выполненного ДЗ отправить ссылку на проект GitHub в котором будет находится код.
"""
path_3 = "Task_3/file.txt"


def numbers(filename):
    digits = []
    current_line = 0
    with open(f"{filename}", "r", encoding="utf-8") as open_file:
        for line in open_file:
            numbers_list = line.split()
            current_line += 1

            for i in numbers_list:
                digit = ''.join([char for char in i if char.isdigit() or char == '.'])
                if digit:
                    digits.append({"number": digit, "line": current_line})

    open_file.close()

    with open("Task_3/g.txt", "w", encoding="utf8") as write_file:
        for i in range(len(digits)):
            write_file.write(f"Число {digits[i]['number']} - строка {digits[i]['line']}\n")


numbers(path_3)
