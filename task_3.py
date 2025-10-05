# Напишіть ітератор, який повертає елементи заданого списку у зворотному порядку (аналог reversed).
class Iterator:
    def __init__(self, my_list: list):
        self.my_list = my_list    

    def __iter__(self):
        self.index = len(self.my_list) - 1      
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = f"{self.index + 1} -  {self.my_list[self.index]}"
        self.index -= 1
        return result
    
my_list = Iterator(["one", "piece", "per", "time", "hello", "world"])

for item in my_list:
    print(item)
