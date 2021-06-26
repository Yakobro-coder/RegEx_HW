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
    return merge_clone(contacts_list)


def merge_clone(contacts_list):
    print(cont_list)
    print(len(cont_list))
    # i = 2
    # for block1 in contacts_list[1:]:
    #     count = i
    #     for block2 in contacts_list[i:]:
    #         if block1[0:2] == block2[0:2]:
    #             for numb in range(0, len(block1)):
    #                 if block1[numb] == '':
    #                     block1[numb] = block2[numb]
    #             del contacts_list[count]
    #             i -= 1
    #         count += 1
    #
    #     i += 1
    #
    i2 = 2
    for block in contacts_list[1:]:
        for index in range(i2, len(contacts_list[1:])):
            print(f'{block[0:2]} =-------= {contacts_list[i2][0:2]}')
            if block[0:2] == contacts_list[i2][0:2]:
                for numb in range(0, len(block)+1):
                    if block[numb] == '':
                        block[numb] = contacts_list[i2][numb]
                del contacts_list[i2]
            i2 += 1
        index = 0

write_fio_in_column(cont_list)
print(cont_list)
print(len(cont_list))
