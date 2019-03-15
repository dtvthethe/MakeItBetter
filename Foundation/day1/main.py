# bai 1:
import random

greeting_text = random.choice(['Xin chao', 'Hello', 'Hi', 'What"s up'])
print(greeting_text)

#bai 2:
k = 8
for i in range(0,k):
    for j in range(0, k - i -1):
        print('   ', end='')
    for z in range(0, i*2 - 1):
        print(' * ', end='')
    print('\n')

'''
  *   2
 ***  1
***** 0
'''