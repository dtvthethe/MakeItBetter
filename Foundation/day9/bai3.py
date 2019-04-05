from ast import literal_eval
from text_utility import read, write

class TaiLieu:
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0):
        self.ma_tl = ma_tl
        self.ten_nxb = ten_nxb
        self.so_ban = so_ban
        self.__loai_tl = 0

    def set_loai_tl(self, loai_tl = 0):
        self.__loai_tl = loai_tl

    def tim_kiem(self, tu_khoa):
        return True if self.ma_tl.lower().__contains__(tu_khoa.lower()) or self.ten_nxb.lower().__contains__(
            tu_khoa.lower()) else False

class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, ten_tg='', so_trang=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        super().set_loai_tl(0)
        self.ten_tg = ten_tg
        self.so_trang = so_trang

    def tim_kiem(self, tu_khoa):
        return True if super().tim_kiem(tu_khoa) else True if self.ten_tg.lower().__contains__(tu_khoa) else False

class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, so_ph=0, thang_ph=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        self.so_ph = so_ph
        self.thang_ph = thang_ph
        super().set_loai_tl(1)

class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, ngay_ph=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        self.ngay_ph = ngay_ph
        super().set_loai_tl(2)

class QuanLTaiLieu:

    def __init__(self):
        self.ds_tai_lieu = []

    def hien_thi(self):
        for tl in self.ds_tai_lieu:
            print(tl.__dict__)

    def tim_kiem(self):
        tu_khoa = str(input('Nhập từ khoá cần tìm: '))
        lst = filter(lambda tl: tl.tim_kiem(tu_khoa), self.ds_tai_lieu)
        for tl in lst:
            print(tl.__dict__)

    def load_dl(self, str_file_data):
        data_rd = read(str_file_data).splitlines()
        for item in data_rd:
            dict_item = literal_eval(item)
            if dict_item['_TaiLieu__loai_tl'] is 0: #Sach
                sach = Sach(dict_item['ma_tl'], dict_item['ten_nxb'], dict_item['so_ban'],dict_item['ten_tg'], dict_item['so_trang'])
                sach.set_loai_tl(0)
                self.ds_tai_lieu.append(sach)
            elif dict_item['_TaiLieu__loai_tl'] is 1: #tap chi
                tapchi = TapChi(dict_item['ma_tl'], dict_item['ten_nxb'], dict_item['so_ban'],dict_item['so_ph'],dict_item['thang_ph'])
                tapchi.set_loai_tl(1)
                self.ds_tai_lieu.append(tapchi)
            elif dict_item['_TaiLieu__loai_tl'] is 2: #bao
                bao = Bao(dict_item['ma_tl'], dict_item['ten_nxb'], dict_item['so_ban'],dict_item['ngay_ph'])
                bao.set_loai_tl(2)
                self.ds_tai_lieu.append(bao)
            else:
                continue


    def ghi_file_json(self, str_file_data):
        str_data = ''
        for tl in self.ds_tai_lieu:
            str_data += str(tl.__dict__)+'\n'
        write(str_file_data, str_data)

qltv = QuanLTaiLieu()
qltv.load_dl('data.json')
int_menu = 1
while int_menu >= 1 and int_menu <= 4:
    print('============================================')
    int_menu = int(input('Chức năng:\n\t1/ Hiển thị dữ liệu\n\t2/ Tìm kiếm\n\t3/ Lưu vào file .json\n\t0/ Thoát\n Lựa chọn: '))
    if int_menu == 1:
        qltv.hien_thi()
    elif int_menu == 2:
        qltv.tim_kiem()
    elif int_menu == 3:
        qltv.ghi_file_json('data.json')
    else:
        break

