def find_common_participants(first_group, second_group, separator =","):
    participants1 = first_group.split(separator)
    participants2 = second_group.split(separator)
    common_participants = set(participants1) & set(participants2)
    result = sorted(common_participants)
    return result


# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
result = find_common_participants(participants_first_group, participants_second_group, separator = "|")
print(result)

# TODO Провеьте работу функции с разделителем отличным от запятой
