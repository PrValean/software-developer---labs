def find_common_participants(participants_1, participants_2, symb=","):
    participants_set_1 = set(participants_1.split(symb))
    participants_list_2 = participants_2.split(symb)

    common = list(participants_set_1.intersection(participants_list_2))

    common.sort()

    return common


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(
    participants_first_group,
    participants_second_group,
    "|"
))
