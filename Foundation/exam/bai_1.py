from collections import Counter


# Doc file:
def read(str_file_path):
    file = None
    text = ''
    try:
        file = open(str_file_path, 'r')
        text = file.read()
    except BaseException as be:
        print(be)
    finally:
        if file:
            file.close()
            return text


# Ghi file
def write(str_file_path, content):
    file = None
    try:
        file = open(str_file_path, 'w')
        file.write(content)
    except BaseException as be:
        print(be)
    finally:
        if file: file.close()


# Xoa trang file:
def erase(str_file_path):
    write(str_file_path, '')


# Dem tong so tu cua file:
def get_number_of_word(str_file_path):
    return len(read(str_file_path).lower().split())


# Dem tong so ki tu cua file:
def get_number_of_character(str_file_path):
    return len(read(str_file_path).lower())


# Dem tong so tu khong trung lap cua file:
def get_number_of_word_not_dublicate(str_file_path):
    int_num = 0
    lst_counter_character = Counter(read(str_file_path).lower().split()).items()
    for character, number_visible in lst_counter_character:
        if number_visible == 1:
            int_num += 1
    return int_num


# Dem tong so ki tu khong trung lap cua file:
def get_number_of_character_not_dublicate(str_file_path):
    int_sum = 0
    lst_counter_character = Counter(list(read(str_file_path).lower())).items()
    for character, number_visible in lst_counter_character:
        if number_visible == 1:
            int_sum += 1
    return int_sum
