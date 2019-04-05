import math

bieu_thuc = '√([(2 * A * B)/C])'
tap_gia_tri = [('A', 5), ('B', 10), ('C', 7.5)]
ket_qua = 0

for item in tap_gia_tri:
    bieu_thuc = bieu_thuc.replace(item[0], item[1].__str__())
bieu_thuc = bieu_thuc.replace('√', 'math.sqrt').replace('[', '').replace(']', '')

exec('ket_qua = ' + bieu_thuc)
print('Ket qua =', ket_qua)
