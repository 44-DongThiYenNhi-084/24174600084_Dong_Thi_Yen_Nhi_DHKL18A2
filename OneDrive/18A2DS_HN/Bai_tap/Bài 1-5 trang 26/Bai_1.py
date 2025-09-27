class hinh_chu_nhat:
    def __init__(self,chieu_dai,chieu_rong):
        self.chieu_dai=chieu_dai
        self.chieu_rong=chieu_rong
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) *2 
    def tinh_dien_tich(self): 
        return( self.chieu_dai * self.chieu_rong )
    def in_thong_tin(self):
        chu_vi=self.tinh_chu_vi()
        dien_tich=self.tinh_dien_tich()
        print(f" Hình chữ nhật có chiêu dài :{self.chieu_dai} và chiều rộng:{self.chieu_rong}, chu vi : {chu_vi} , dien tich: {dien_tich}")
chieu_dai=float(input("Nhập vào chiều dài: "))
chieu_rong=float(input("Nhập vào chiều rộng: "))
Hc_n=hinh_chu_nhat(chieu_dai,chieu_rong)
Hc_n.in_thong_tin()




