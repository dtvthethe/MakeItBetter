from text_utility import read

# 1) Xay dung cac lop de quan ly tai lieu
class TaiLieu:
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0):
        self.ma_tl = ma_tl
        self.ten_nxb = ten_nxb
        self.so_ban = so_ban

    def tim_kiem(self, tu_khoa):
        return True if self.ma_tl.lower().__contains__(tu_khoa.lower()) or self.ten_nxb.lower().__contains__(
            tu_khoa.lower()) else False


class Sach(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, ten_tg='', so_trang=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        self.ten_tg = ten_tg
        self.so_trang = so_trang

    def tim_kiem(self, tu_khoa):
        return True if super().tim_kiem(tu_khoa) else True if self.ten_tg.lower().__contains__(tu_khoa) else False


class TapChi(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, so_ph=0, thang_ph=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        self.so_ph = so_ph
        self.thang_ph = thang_ph


class Bao(TaiLieu):
    def __init__(self, ma_tl='', ten_nxb='', so_ban=0, ngay_ph=0):
        super().__init__(ma_tl, ten_nxb, so_ban)
        self.ngay_ph = ngay_ph

# 2) Xay dung lop QuanLTaiLieu
class QuanLTaiLieu:

    def __init__(self):
        self.ds_tai_lieu = []

    def nhap_thong_tin_tai_lieu(self):
        str_next = '1'
        while (str_next == '1'):
            loai = int(input('Loại tài liệu:\n\t0/ Sách\n\t1/ Tạp chí\n\t2/ Báo\nLoại tài liệu: '))
            ma_tl = str(input('Mã tài liêu: '))
            ten_nxb = str(input('Tên nhà xuất bản: '))
            so_ban = int(input('Số bản phát hành: '))
            if loai == 0:  # Sách
                ten_tg = str(input('Tên tác giả: '))
                so_trang = int(input('Số trang: '))
                self.ds_tai_lieu.append(Sach(ma_tl, ten_nxb, so_ban, ten_tg, so_trang))
            elif loai == 1:  # Tạp chí
                so_ph = int(input('Số phát hành: '))
                thang_ph = int(input('Tháng phát hành: '))
                self.ds_tai_lieu.append(TapChi(ma_tl, ten_nxb, so_ban, so_ph, thang_ph))
            elif loai == 2:  # Báo
                ngay_ph = int(input('Ngày phát hành: '))
                self.ds_tai_lieu.append(Bao(ma_tl, ten_nxb, so_ban, ngay_ph))

            str_next = str(input('Nhập "1" để tiếp tục: '))

    def hien_thi(self):
        for tl in self.ds_tai_lieu:
            print(tl.__dict__)

    def tim_kiem(self):
        tu_khoa = str(input('Nhập từ khoá cần tìm: '))
        lst = filter(lambda tl: tl.tim_kiem(tu_khoa), self.ds_tai_lieu)
        for tl in lst:
            print(tl.__dict__)

    def tao_dl_tu_dong(self, str_file_data):
        txt = read(str_file_data)
        for line in txt.split('\n'):
            arr_line = line.split(';')
            if arr_line[0] is '0':  # Sach
                self.ds_tai_lieu.append(Sach(arr_line[1], arr_line[2], int(arr_line[3]), arr_line[4], int(arr_line[5])))
            elif arr_line[0] is '1':  # Tap chi
                self.ds_tai_lieu.append(
                    TapChi(arr_line[1], arr_line[2], int(arr_line[3]), int(arr_line[4]), int(arr_line[5])))
            elif arr_line[0] is '2':  # Bao
                self.ds_tai_lieu.append(Bao(arr_line[1], arr_line[2], int(arr_line[3]), int(arr_line[4])))
            else:
                pass


qltv = QuanLTaiLieu()
int_menu = 1
while int_menu >= 1 and int_menu <= 4:
    print('============================================')
    int_menu = int(input('Chức năng:\n\t1/ Nhập thông tin tài liệu\n\t2/ Tạo dữ liệu từ động\n\t3/ Hiển thị dữ liệu\n\t4/ Tìm kiếm\n\t0/ Thoát\n Lựa chọn: '))
    if int_menu == 1:
        qltv.nhap_thong_tin_tai_lieu()
    elif int_menu == 2:
        qltv.tao_dl_tu_dong('data.txt')
    elif int_menu == 3:
        qltv.hien_thi()
    elif int_menu == 4:
        qltv.tim_kiem()
    else:
        break

