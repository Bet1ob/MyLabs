# TODO Напишите функцию для поиска индекса товара

list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
item = 'груша'

def poisk(list,item):
    index = 0
    for i in range(len(list)):
        if item in list[i]:
            index=i
            break
    if index==0:
        index=None
    return index



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = poisk(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
