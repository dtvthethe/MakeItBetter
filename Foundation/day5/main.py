from bai1 import get_fibonacci
from bai2 import get_most_common_used_word, get_words_next_to_right

# Bài 1:
int_number = 10
for i in range(0, int_number):
    print(get_fibonacci(i), end=', ')

# Bài 2:
str_file_path = 'data.txt'
str_find_by_word = 'the'

most_used_word = get_most_common_used_word(str_file_path)
print('\n\nTừ xuất hiện nhiều nhất: "%s", số lần xuất hiện: %d' %(most_used_word[0], most_used_word[1]))

lst_words = get_words_next_to_right(str_file_path, str_find_by_word)
print('\nDanh sách từ xuất hiện bên phải của từ "%s":' %str_find_by_word)
for (word, number_of_time_appear) in lst_words:
    print('"%s" -> %d' %(word.split()[1], number_of_time_appear))