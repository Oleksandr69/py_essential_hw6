# Взявши за основу код прикладу example_5.py, розширте функціональність класу MyList,
# додавши методи очищення списку, додавання елемента у довільне місце списку,
# видалення елемента з кінця та довільного місця списку.

class MyList(object):
    """Класс списка"""
    class _ListNode(object):
        """Внутренний класс элемента списка"""
        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value, id(self.prev), id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration
            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None

        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""
        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)
    
    def clear(self):
        self._head = self._tail = None
        self._length = 0
    # Додавання елемента за індексом.
    def insert_by_index(self, my_value, index):
        node = self._head
        my_node = MyList._ListNode(my_value)
        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node.value
        else:
            if not 0 <= index < len(self):
                raise IndexError('list index out of range')
            for _ in range(index - 1):
                # print("node.value - ", node.value)
                # print("node.next - ", node.next)
                node = node.next
            my_node.prev = node.value
            my_node.next = node.next
            node.next = my_node
            self._length += 1

    def delete_by_index(self, index):
        node = self._head     
        if self._tail is None:
            print("Список порожній")
        else:
            if not 0 <= index < len(self):
                raise IndexError('list index out of range')
            for _ in range(index - 1):
                node = node.next
                my_node = node.next
            # print("node- ", node)
            # print("my_node- ", my_node)
            node.next = my_node.next
            # print("my_node after- ", my_node)
            # print("node.next- ", node.next)
            self._length -= 1
      
def main():
    # Создание списка
    print("================creation=========")
    my_list = MyList(["1", "2", "5", "7", "12", "57", "66", "77"])
    print("==my_list._head- ", my_list._head)
    print("==my_list._tail- ", my_list._tail)
    print("1- len(my_list)- ", len(my_list))
    print("1- my_list- ", my_list)
    print("1- element in my_list: ")
    for element in my_list:
        print("*", element)
    print("================insert by index=========")
    my_list.insert_by_index("9", 2)
    my_list.insert_by_index("17", 4)    
    print("2- len(my_list)- ", len(my_list))
    print("2- my_list- ", my_list)
    print("2- element in my_list: ")
    for element in my_list:
        print("*", element)
    print("================delete by index=========")
    my_list.delete_by_index(8)
    my_list.delete_by_index(8)
    print("3- len(my_list)- ", len(my_list))
    print("3- my_list- ", my_list)
    print("3- element in my_list: ")
    for element in my_list:
        print("*", element)
    print("================clear=========")
    my_list.clear()
    print("4- len(my_list)- ", len(my_list))
    print("4- my_list.clear- ", my_list)
    print("4- element in my_list- ")
    for element in my_list:
        print("*", element)
    print("=============================================")

if __name__ == '__main__':
    main()

