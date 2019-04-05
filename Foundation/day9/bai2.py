import re

re_pattern = r'^(?=.{8,})(?=.*[A-Z]{1,})(?=.*[a-z]{1,})(?=.*\d)(?=.*[~!@#$%^&*()_+{}|:"?><,./;\'\[\]\\=\-\`]{1,}).*$'

arr_data_test_case = ['You1Tu2Be3@', 'YouTuBe@', 'you1tu2be3@', 'You1Tu2Be3', 'You1@', 'YOU1TU2BE3@',
                      'You1Tu 2Be3@', 'You1Tu2Be3@You1Tu2Be3@You1Tu2Be3@You1Tu2Be3@You1Tu2Be3@']

for pw in arr_data_test_case:
    if re.match(re_pattern, pw):
        print('%s -> OK' %pw)
    else:
        print('%s -> Wrong format' % pw)