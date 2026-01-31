# TODO Напишите функцию для поиска индекса товара
def index(list, item):
    for a, b in enumerate(list): #перебор элементов списка с их индексами
        if b == item: #если элемент совпадает с искомым товаром,то возврат его индекса
            return a

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index(items_list,find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
