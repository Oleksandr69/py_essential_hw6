# Реалізуйте цикл, який перебиратиме всі значення ітерабельного об'єкту iterable
my_list = ["one", "piece", "per", "time"]
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
index = 0
while index < len(my_list):
    print(next(my_iter))
    index += 1

