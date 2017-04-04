#A common idiom to change every element of a list looks like this:
'''
tup = (['this', 'is', 'a list', 'in a tuple'], ['another', 'one', 'bruv'], ("can't change this"))


change = tup[0].append(1)

print(tup)

test = '\directory\is\here'

print(test)


'''
'''
import os

data = input("What would you like to put into the file? ")

try:
    directory = "/Users/KennyB/Desktop/testingMe/"
    filename = "sheet.txt"
    full_path = directory + filename

    # make directory
    if os.path.exists(directory):
        print("directory already created..moving on")
    else:
        os.mkdir(directory)
    # make file
    if os.path.isfile(full_path):
        print("file already created...moving on")
    else:
        with open(full_path, 'w'):
            pass
    with open(full_path, 'a+') as f:
        f.write('\n' + data + '\n')

except OSError as e:
    print(e)
'''


# here is an example of a good recursion function. It will list the contents of a directory, then check to see if there
# are directories within the directory. Once determined, the function will either print all items in a folder, or go
# deeper within another folder and print all those contents
# the os.join method can be used cross-platform - remember directory structures are different in linux and windows
# remember, recursion is where the solution of a problem depends on solutions of smaller instances of the same problem,
# and involves a function calling itself in that same function
# as opposed to iteration which is a block of code meant to repeat over and over, not based on outcome
#
'''
path = "/Users/KennyB/Desktop/"

def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath): # iterate thru items in path provided
        sChildPath = os.path.join(sPath, sChild) # to check if item is a subdirectory, join the original path and child
        if os.path.isdir(sChildPath): # if the file is indeed a subdirectory, interate and display those conents too
            print_directory_contents(sChildPath) # again, list conents in child path
        else:
            print(sChildPath) # print full path. This should eventually hit every time


print_directory_contents(path)

'''
'''

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print(res)
        return res

print(factorial(5))


def rec(n):
    if n != 1 or 0:
        print(n)
        result = n * rec(n-1)
        return result
    else:
        print("Done")
        return 1


l1 = [0,1,2]

l2 = l1

l2.append(600)
print(l1)
print(l2)

def my_function(*args, **kwargs):
    print(kwargs)
    for v in kwargs.values():
        print("{} + 5 = ".format(v), v + 5)
    print(args)
    for v in args:
        print("{} + 10 = ".format(v), v + 10)


print(my_function(1,2,3,4,5,6,7,8,9,a=13, b=56))


'''

'''
def my_function():
    print("first in my function")
    def my_second_function():
        print("second in my function")
        def my_third_function():
            print("my 3rd function")
    return my_second_function
'''

import datetime

new_list = []

#def add(num):
#    return num + 2

'''
def timestamp(original_function):
    def new_function(*args, **kwargs):
        before = datetime.datetime.now()
        x = original_function(*args, **kwargs)
        after = datetime.datetime.now()
        print("Function: {0} has an execution time of: {1}".format(original_function.__name__,after-before))
        return x
    return new_function


@timestamp
def funca(*args, **kwargs):
    new_list = [i for i in range(1,100001)]
    new_dict = {i: chr(65+i)for i in range(400)}
    print(new_dict)

@timestamp
def funcb(*args, **kwargs):
    new_list = [int(i + 3 * 80000 / 3 + 8 / 3) for i in range(1,1001)]
    new_dict = [i + 120 for i in new_list]
    #print(new_list)
    #for i in range(1,100001):
    #    new_num = int(i + 3 * 80000 / 3 + 8 / 3)
    #    new_list.append(new_num)
@timestamp
def funcc():
    my_list = []
    my_new_list = [my_list.append(int(i + 3 * 800000000 / 3 + 8 / 3)) for i in range(1,1000)]
    print(my_list)

funca()
funcb()
funcc()
#x = timestamp(x)
#print(x)
'''

'''
def except_error(function):
    def new_function(*args, **kwargs):
        try:
            x = function(*args, **kwargs)
        except (ValueError, TypeError) as e:
            print("Error. Please use only numbers. The following error has occurred: {}".format(e))
        return function
    return new_function


@except_error
def add(*args, **kwargs):
    [print(int(i) * 100) for i in args]


add(3,5,6,6,9)



class Switch:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address
        self.models = {}
    def add_models(self, *args):
        if len(args) > 9:
            print("Too many switches entered. There is a max of 9 switches supported")
        else:
            switch_num = 1
            for model in args:
                self.models[switch_num] = model
                switch_num +=1





switch1 = Switch("USAAKKIDF1001", "172.168.1.1")
switch1.add_models('ws-3850-48p','ws-3850-24t','ws-3850-24p','ws-3850-48t','ws-3850-24t','ws-3850-24p','ws-3850-48t',
                   'ws-3850-24t', 'ws-3850-24p')

print(switch1.hostname)
print(switch1.ip_address)
print(switch1.models)


def test():
    return 8 * 2

x = test()
print(x)


source_file_one = '/Users/KennyB/Desktop/testingMe/blah1.txt'
source_file_two = '/Users/KennyB/Desktop/testingMe/blah2.txt'


def compare(source_file_one, source_file_two):
    list1 = []
    list2 = []
    hostnames = []
    ip_addresses = []
    with open(source_file_one) as f:
        source_file_data_one = f.readlines()
        for chr in source_file_data_one:
            list1.append(chr.strip("\n"))
    with open(source_file_two) as f:
        source_file_data_two = f.readlines()
        for chr in source_file_data_two:
            list2.append(chr.strip("\n"))
    difference = set(list1) ^ set(list2)
    for i in difference:
        if 'hostname' in i:
            hostnames.append(i)
        if 'ip address' in i:
            ip_addresses.append(i)
    return hostnames, ip_addresses


def output(hostnames, ip_addresses):
    print("---------------------")
    if hostnames:
        print("Hostname Differences: \n")
        for hostname in hostnames:
            print(hostname)
        print("---------------------")
    if ip_addresses:
        print("IP Address Differences: \n")
        for ip in ip_addresses:
            print(ip)
        print("---------------------")



#    difference = set(list1) ^ set(list2) # both set elements show that are different
#    for diff in sorted(difference):
#        print(diff.strip(" "))



hostnames, ip_addresses = compare(source_file_one, source_file_two)
output(hostnames, ip_addresses)

import abc





person = {'name': 'Kenneth', 'age': 23, 'occupation': 'network engineer'}

try:
    print('My name is {name} and I am {age} years old and I work as a {occupation}.'.format(**person))
except KeyError as e:
    print(e)


data = "This is a sentence."
re_find = re.compile("^.*e.*$")
result = re.findall(re_find, data)
if result and len(result) == 1 :
    print("{} match found!".format(len(result)))
elif result:
    print("{} matches found!".format(len(result)))
else:
    print("no match found!")
'''
'''
import re


config_file = '/Users/KennyB/Desktop/testingMe/blah3.txt'
with open(config_file) as f:
    #config_lines = f.readlines()
    config_lines = [i for i in enumerate(f, 1)] # start emueration at 1, because starting at line 1 is easier for humans



# use list comprehension to search thru config file. m.group(0) always returns matched regex. You are saying here, for
# each line in the data list, use regex to search each line, and exclude any other values by using if match
#print(config_lines)
#regex = re.compile("^.*ip address")
regex = re.compile("^Processor")
#data = [match.group(0) for line in config_lines for match in [regex.findall(line[1])] if match]

#line[1].split(" ") - look inside tuples, look at second value, split spaces, then look at the 3rd index (where serial
#number is). Do this for each line that matches ^Processor and add to serial_number list if it matches
serial_number = [line[1].split(" ")[2].strip("\n") for line in config_lines for match in [regex.findall(line[1])] if match]
print(serial_number[0])

#result = re.search(re_find, data)
#print("{} match found!".format(result))

'''

#
# class Employee:
#     def __init__(self, first_name, last_name, job, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.job = job
#         self.salary = salary
#
#     @property
#     def total_compensation(self):
#         return self.salary * .20 + self.salary
#
#     @property
#     def email_address(self):
#         return "{}.{}@abccompany.com".format(self.first_name, self.last_name)
#
#     @property
#     def full_name(self):
#         return "{} {}".format(self.first_name, self.last_name)
#
#     @full_name.setter
#     def full_name(self, name):
#         first_name, last_name = name.split(' ')
#         self.first_name = first_name
#         self.last_name = last_name
#
#
#
#
# ken = Employee('Kenneth', 'Buchanan', 'Network Engineer', 100000)
# ken.first_name = 'Kenny'
# print(ken.total_compensation)
# print(ken.email_address)
# ken.full_name = 'John Hopkins'
# print(ken.full_name)
# print(ken.email_address)
#
#
#
# class Airplane(object):
#     def __init__(self, model, serial_number, wingspan, avg_speed):
#         self.model = model
#         self.serial_number = serial_number
#         self.wingspan = wingspan
#         self.avg_speed = avg_speed
#
#     @property
#     def top_speed(self):
#         return self.avg_speed - 50
#
#
# class Fighter_Jet(Airplane):
#     def __init__(self, model, serial_number, wingspan, avg_speed, bullet_type):
#         self.bullet_type = bullet_type # declare new property just for Fighter_jet class
#         super().__init__(model, serial_number, wingspan, avg_speed) # properties to bring in from parent
#
#     @property
#     def top_speed(self):
#         return self.avg_speed + 10000
#
#     def __repr__(self):
#         return "Blah"
#
#     def __str__(self):
#         return "Plane model: {} Wingspan: {} Average Speed: {}".format(self.model, self.wingspan, self.avg_speed)
#
#
#
# airplane = Airplane('BOEING-B39N-NAM', '4920GFAF31', 35, 543)
# print(airplane.model, airplane.top_speed)
# print(airplane)
#
#
# fighter_jet = Fighter_Jet('LOCKHEED-990FB', 'FF298UYFN', 18, 898, '44mm')
# print(fighter_jet.model, fighter_jet.top_speed, fighter_jet.bullet_type)
# print(fighter_jet)
#
#
#
#
# import os
#
# file_check = os.path.isfile('/Users/KennyB/Desktop/testingMe/')
# dir_check = os.path.isdir('/Users/KennyB/Desktop/testingMe/blah.txt')
#
# if file_check:
#     print("Yes")
# else:
#     print("No")
#
#
# cwd = os.getcwd()
#
# for cpath, dirs, files in os.walk(cwd):
#    if cpath == '/Users/KennyB/Google Drive/Personal/Code/python/network_scripts':
#        if dirs:
#            print("There are directories here: {}".format(dirs))



# key = 'A73902020'
# yes = 'YES'
#
# dict_key = dict(dictkey=key, thisIsCool=yes)
#
# print(dict_key)
#
# this = '1'
# try:
#     print(int(this))
#     raise print("raise")
# except ValueError as e:
#     print(e)

# data = 1
# hey = data or ['this', 'that']
# print(hey)
#
#
# # yes, this is my code for practice :)
#
# def except_error(function):
#     def new_function(*args, **kwargs):
#         funct = function(*args, **kwargs)
#         for i in args:
#             try:
#                 int(i)
#             except (ValueError, TypeError) as e:
#                 print("Error. Please use only numbers. The following error has occurred: {}".format(e))
#         return function
#     return new_function
#
# @except_error
# def add(*args, **kwargs):
#     print(kwargs)
#     answer_nums = [n for n in args]
#     answer_strs = [s for s in kwargs]
#     return (answer_nums, answer_strs)
#
#
# add(3,5,6,6,9,125125,'b',223,12,13,342,53,53,53,4,2,3,13,112,129,4,1,'a', caw='baw')
#
#
#
# my_dict = {'a_key': 'a_value', 'b_key': 'b_value'}
#
# for i in my_dict.values():
#     print(i)



print('-----mississippi----'.strip('-'))

import re

text = 'caw001        '
check = re.sub(r'..\d\s+$', "caw", text)
print(check)

import os
from shutil import copyfile

main_dir = '/Users/KennyB/Downloads'
# target_dir = os.path.join(main_dir, 'Python Files')
# new_dir = os.path.join(target_dir, 'Python Files Copy')

# for cdir, dirs, files in os.walk(main_dir):
#     if cdir == target_dir:
#         os.chdir(target_dir)
#         if os.path.exists(new_dir):
#             pass
#         else:
#             os.mkdir(new_dir)
#         for file in files:
#             old_file_path, new_file_path = os.path.join(target_dir, file), os.path.join(new_dir, file)
#             old_filename, file_extension = os.path.splitext(file)
#             new_filename = os.path.join(target_dir, old_filename) + '-Copy' + file_extension
#             copyfile(old_file_path, new_file_path)
#             os.rename(old_file_path, new_filename)

# recursive loop for scanning paths for files and directories, counts number of files too
file_cnt = 0
dir_cnt = 0
hid_file_cnt = 0

def scan_folders(directory):
    '''scans for all files and directories recursively. Provides count of files/folders and hidden'''

    global dir_cnt, file_cnt, hid_file_cnt

    try:
        for object in os.scandir(directory): # scan specified directory
            if object.is_dir() and not object.name.startswith('.'): # find all directories, omit hidden
                dir_cnt += 1
                scan_folders(os.path.join(directory, object.name))
            elif object.is_file and not object.name.startswith('.'): # find all files, omit hidden
                file_cnt += 1
            elif object.is_file: # find remaining hidden files
                hid_file_cnt +=1
    except OSError as e:
        print(e)

print(scan_folders("/Users/KennyB/Pictures"))
print("Number of files :", file_cnt)
print("Number of directories:", dir_cnt)
print("Number of hidden files/folders:", hid_file_cnt)


# caw = [1,2,3,4]
#
# for num in caw:
#     if num == 10:
#         break
#     else:
#         raise TypeError

text = 'caw'

class MyClass(object):

    def __init__(self, height, weight=100):
        self.height = height
        self.weight = weight

    def expand_height(self, height):
        self.height = height * 10000000


caw = MyClass(40)

print(getattr(caw, 'weight'))
caw.weight = 4000


print(getattr(caw, 'height'))
caw.expand_height(3000)
print(getattr(caw, 'height'))


my_dict = {'key_1': 'value_1','key_2': 'value_2','key_3': 'value_3','key_4': 'value_4','key_5': 'value_5',}

caw = my_dict.get('key_1', 'blah')

print(caw)

