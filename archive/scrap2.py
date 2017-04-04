'''
list = ['caw', 'baw', 'taw',' naw']


print(list[1:])

'''


# my_dict = {"caw": 1, "baw": 2, "law": 3}
#
# new_dict = {k: v * 2 for k,v in my_dict.items()}
#
# print(new_dict)
#
# for k,v in my_dict.items():
#     print(k, v)
#
# import itertools
#
# list_1 = ["this", "is", "a", "list"]
# list_2 = ["cat", "dog", "mouse"]
#
# # zipped = itertools.zip_longest(list_1, list_2)
# #
# #
# # print(dict(zipped))
# #
# # list_3 = [1, 2, 3, 4, 5, 6, 7, 8]
# #
# # print(list(filter(lambda x:x  % 2 == 0, list_3)))

import functools

# my_list = range(1, 101)
#
#
# sum = 0
# for i in my_list:
#     sum += i
#
# print(sum)
#
# num = 100 * (100 + 1) / 2
# print(num)
#
# def sum_of_all_evils(n):
#     return n * (1 + n) / 2
#
# result = sum_of_all_evils(5)
#
# print(result)
#
# def first_funct(x):
#     z = 10
#     def second_funct(y):
#         return x * y * z
#     return second_funct
#
# mult_by_three = first_funct(500)
#
# print(mult_by_three(4))


# def stepper_two(start=1, step=1, end=10000):
#     while start < end:
#         yield (start + 100 / 3 * 3 ** 2 * 400 + 3 / 8 - 52 * 57 * 88 * -1)
#         start += step
#
# caw = stepper_two(start=1, step=1)
#
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
# # print(next(caw))
#
# for num in range(1,30):
#     step = next(caw)
#     print(step)





# def stepper(maximum):
#     i = 0
#     while i < maximum:
#         val = (yield i)
#         # If value provided, change counter
#         if val is not None:
#             i = val
#         else:
#             i += 1
#
#
#
# this = stepper(10)
# print(next(this))
# print(next(this))

# from datetime import datetime
#
#
#
# my_nums = (x*x for x in range(1,20000000))
# my_list = []
# my_list_two = []
# my_list_three = []
#
# before = datetime.now()
#
# for x in my_nums:
#     if x % 2 == 0:
#         my_list_two.append(x)
#
# after = datetime.now()
# print(after - before)
#
#
#
# before = datetime.now()
#
# for x in range(1,20000000):
#     x = x * x
#     my_list.append(x)
#
# for num in my_list:
#     if num % 2 == 0:
#         my_list_three.append(num)
#
# after = datetime.now()
# print(after - before)

# from itertools import count
#
# counter = count(1,10)
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# ls = ['one', 'two', 'three']
#
# ls[ls.index('one')] = 'hello'
#
# print(ls)

from functools import reduce
from itertools import groupby
animal_kingdom = [
    {'animal': 'fox', 'name': 'Charles'},
    {'animal': 'rabbit', 'name': 'Yang'},
    {'animal': 'whale', 'name': 'Chad'},
    {'animal': 'dog', 'name': 'Mike'},
    {'animal': 'wombat', 'name': 'Dave'},
    {'animal': 'wombat', 'name': 'Mark'},
    {'animal': 'wombat', 'name': 'Brad'},
    {'animal': 'wombat', 'name': 'Tom'},]

# mapped_dict = dict(map(lambda x: x.items(), animal_kingdom))
# mapped_list = list(map(lambda x: x.items(), animal_kingdom))
# reduced = reduce(lambda y, z: y + z, mapped_dict)
# print(reduced)
# sorted = mapped_list
# print(sorted)
# grouped_dict = list(groupby(animal_kingdom, key=lambda x: x['animal']))
# print(grouped_dict)
# grouped = groupby(animal_kingdom, key=lambda x: x['animal'])
# print({k:list(v) for k, v in grouped})


# for item in animal_kingdom:
#     for k, v in item.items():
#         if k == 'name':
#             print(v)
#
#
# print(reduce(lambda x, y: x + y, range(1,101)))


dict_two = {'animal': 'fox', 'name': 'Charles'}
admin = "default_name"

# the following is an if statement checking all keys for 'name' then printing the value of the 'name' key
if 'name' in dict_two.keys():
    print(dict_two['name'])
else:
    print(admin)

# however as you can see here, you can do this with way less lines of code:
found = dict_two.get('name', admin)
print(found)

my_list = ['caw', 'baw', 'taw']
mapped_list = map(lambda x: x, my_list)
print(next(mapped_list))
reduced = reduce(lambda x, y: x + y[1], mapped_list)
print(reduced)

nums = range(1,101)

num_iterator = filter(lambda x: x % 2 ==0, nums)

for i in range(1, 26):
    next(num_iterator)

print(list(num_iterator))

try:
    print("hey")
except TypeError:
    print("error")
finally:
    print("finally!")

