# coding=utf-8
def get_mapp():
    mapp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return mapp
def simple_num_check(x):
    if not isinstance(x,int):
        return
    elif x < 1:
        return False
    else:
        i = x - 1
        while i >= 1:
            if x % i == 0 and i != 1:
                return False
            i -= 1
        return True

def simple_num_seq(max):
    seq = []
    i = 2
    while seq.__len__() != max:
        if simple_num_check(i):
            seq.append(i)
        i += 1
    return seq

def get_mapp_dict(key_list,val_list,n):
    data = {}
    for i in range(n):
        data.setdefault(key_list[i],val_list[i])
    return data


MAPP = {'a': 2, 'c': 5, 'b': 3, 'e': 11, 'd': 7, 'g': 17, 'f': 13, 'i': 23, 'h': 19, 'k': 31, 'j': 29, 'm': 41, 'l': 37, 'o': 47, 'n': 43, 'q': 59, 'p': 53, 's': 67, 'r': 61, 'u': 73, 't': 71, 'w': 83, 'v': 79, 'y': 97, 'x': 89, 'z': 101}
N = 10
LIST = [None]*N
def get_index(string):
    count = 0
    for i in range(len(string)):
        char = string[i]
        summ = MAPP.get(char) if char in MAPP else 0
        count += summ
    index = count % N
    return index
def add_to_hash(key,value):
    index = get_index(key)
    LIST[index] = value
def get_from_hash(key):
    index = get_index(key)
    return LIST[index]






class Data_array:
    def __init__(self, length):
        # self.slot_length = 5
        self.slot = [] # массив одной ячейки основного хранилища

        self.length = length
        self.data_array = [self.slot] * self.length # основное хранилище

        self.kz = 0
        self.used_indexes = 0 # заполненные ячейки
        self.values_inserted = 0 # все ячейки
    def make(self):
        return self.data_array

    def put(self, index, value):
        target_slot = self.data_array[index]
        target_slot.append(value)
    def get(self,index):
        return self.data_array[index]




class Hash:
    def __init__(self):
        self.data_array_length = 10
        self.data_array = [None] * self.data_array_length
        self.added_values = 0
        self.added_keys = 0

    def hash_func(self,string):
        return get_index(string)

    def set(self,key, value):
        self.added_keys += 1
        index = get_index(key)
        LIST[index] = value

    def get(self,key):
        index = get_index(key)
        return LIST[index]


def sort_data(list_of_tupl):
   if list_of_tupl.__len__() < 2:
       return list_of_tupl
   else:
       mid = list_of_tupl.__len__()/2
       o = list_of_tupl[mid]
       less = [pair for pair in list_of_tupl if pair[1] <o[1]]
       more = [pair for pair in list_of_tupl if pair[1] > o[1]]
       return sort_data(less) + [o] + sort_data(more)

import random
if __name__ == '__main__':
    mapp = get_mapp()
    for i in range(1,10):
        mapp.append(str(i))
    data = {}
    length = simple_num_seq(len(mapp))
    for i in range(len(mapp)):
        data.setdefault(mapp[i],length[i])
    print dict(sort_data(data.items()))






