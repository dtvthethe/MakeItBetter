so_tien = 8280000

# Xử lý
doc_so = ['Không', 'Một', 'Hai', 'Ba', 'Bốn', 'Năm', 'Sáu', 'Bảy', 'Tám', 'Chín']
doc_vi_tri = ['đồng', 'mươi', 'trăm', 'nghìn', 'mươi', 'trăm', 'triệu', 'mươi', 'trăm', 'tỷ']

so_tien_chuoi = str(so_tien)

so_tien_str = ''
for idx, c in enumerate(so_tien_chuoi):
    so_tien_str += doc_so[int(c)] + ' '
    so_tien_str += doc_vi_tri[len(so_tien_chuoi) - idx - 1] + ' '

# Làm đẹp
so_tien_str = so_tien_str.replace('Không trăm Không mươi Không đồng', 'đồng chẳn')
so_tien_str = so_tien_str.replace('Không mươi', 'lẽ')

# output
print(so_tien_str)

def abc(a, b):
    '''
    anc]ak kaw
    :param a:
    :param b:
    :return:
    '''
    # global so_tien
    so_tien = 1280

abc()
print(so_tien)