
# TODO Напишите функцию find_common_participants

def find_common_participants(first, second, arg = ','):
    list1 = first.split(arg) #разделение строки по заданному разделителю
    list2 = second.split(arg)
    allpart = list(set(list1).intersection(list2)) #нахождение пересечения участников из двух групп
    allpart.sort() #сортировка списка
    return allpart #возвращение отсортированного списка

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


# TODO Проверьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group))