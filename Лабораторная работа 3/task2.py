# TODO Напишите функцию find_common_participants
def find_common_participants(list1, list2, razdel=","):
    newlist1 = list1.split(razdel)
    newlist2 = list2.split(razdel)
    Complist = []
    for i in range(len(newlist1)):
        for j in range(len(newlist2)):
            if newlist1[i] == newlist2[j]:
                Complist.append(newlist1[i])

    return sorted(Complist)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

g=find_common_participants(participants_first_group, participants_second_group)
print(g)
# TODO Провеьте работу функции с разделителем отличным от запятой
