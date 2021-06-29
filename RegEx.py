import re
from pprint import pprint
import csv


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
    pattern = re.compile(
        '\+?(\d{1,1})\s?\(?(\d{3,3})\)?\s?-?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})\ *\(*([ \(доб.]*\d{4,4})*[)]*')
    for block in contacts_list:
        if len(block[5]) < 20:
            block[5] = pattern.sub(r'+7(\2)\3-\4-\5', block[5])
        elif len(block[5]) > 20:
            block[5] = pattern.sub(r'+7(\2)\3-\4-\5 \6', block[5])

    return contacts_list


# print(regex_phone(merge_clone(write_fio_in_column(cont_list))))


if __name__ == '__main__':
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        cont_list = list(rows)

    with open("fixed_phonebook.csv", "w") as f:
        data_writer = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        data_writer.writerows(regex_phone(merge_clone(write_fio_in_column(cont_list))))
