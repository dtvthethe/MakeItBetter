check_string = "Con ngựa đá con ngựa đá. Con ngựa đá không đá con ngựa"
# a)
dictword = []
for charss in check_string.strip().split(' '):
    dictword.append((charss,check_string.count(charss)))
result = sorted(dictword, key=lambda word:word[1], reverse=1)
print('từ lặp nhiều nhất : ',result[0][0],', số lần lặp : ', result[0][1])
#b )
dictword2 = []
input_word = input('Nhập từ bất kỳ : ')
string_left_word = check_string[check_string.index(input_word):]
for charsss in string_left_word.strip().split(' '):
   dictword2.append((charsss,string_left_word.count(charsss)))
print(dictword2)