# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
my_list = ["one", "piece", "per", "time", "hello", "world"]
my_iter = iter(my_list)
# for item in my_iter:
#     print(item)
print(my_list)
print(my_iter)
print('')
for item in my_list:
    print(item)
# print("")
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
print("")
# index = 0
# while index < len(my_list):
#     print(next(my_iter))
#     index += 1
# for i in range(len(my_list)):
#     print(my_iter.__next__())
print(my_iter.__dir__())
print(my_iter.__iter__())
print(my_iter.__str__())
print(my_iter.__class__)
print("")
while True:
    try:
        print("--", next(my_iter))
    except StopIteration:
        break

