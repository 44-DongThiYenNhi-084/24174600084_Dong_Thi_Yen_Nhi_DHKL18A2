class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa 

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, "
              f"Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}, "
              f"Tổng điểm: {self.tinh_tong_diem()}")
ds_thi_sinh = []
sl = int(input("Nhập số lượng thí sinh: "))

for i in range(sl):
    print(f"\nNhập thông tin thí sinh {i+1}:")
    ho_ten = input("Họ tên: ")
    diem_hoa = float(input("Điểm Hóa: "))
    diem_ly = float(input("Điểm Lý: "))
    diem_toan = float(input("Điểm Toán: "))
    ts = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
    ds_thi_sinh.append(ts)
ds_trung_tuyen = [ts for ts in ds_thi_sinh if ts.tinh_tong_diem() > 20]
ds_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

print("Danh sách trúng tuyển:")
for ts in ds_trung_tuyen:
    ts.in_thong_tin()
