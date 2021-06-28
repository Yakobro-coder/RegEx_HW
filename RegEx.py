from pprint import pprint
import csv

with open('phonebook_raw.csv', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=',')
    cont_list = list(rows)


def write_fio_in_column(contacts_list):
    for block in contacts_list[1::]:
        fio = block[0]
        if len(block[1]) > 1:
            fio += ' ' + block[1]
        if len(block[2]) > 1:
            fio += ' ' + block[2]
        f_i_o = fio.split(' ')
        try:
            block[0] = f_i_o[0]
            block[1] = f_i_o[1]
            block[2] = f_i_o[2]
        except IndexError:
            pass
        # print(block)
    return contacts_list


def merge_clone(contacts_list):
    del_list = []
    for num1, block1 in enumerate(contacts_list[1:], 1):
        for num2, block2 in enumerate(contacts_list[1:], 1):
            if block1[0:2] == block2[0:2] and num1 != num2 and block1[0] != 0:
                for numb in range(0, len(block1)):
                    if block1[numb] == '':
                        block1[numb] = block2[numb]
                    block2[numb] = 0
                del_list.append(num2)

    for i in list(reversed(sorted(del_list))):
        del contacts_list[i]

    return contacts_list


def regex_phone(contacts_list):
    pass


print(merge_clone(write_fio_in_column(cont_list)))