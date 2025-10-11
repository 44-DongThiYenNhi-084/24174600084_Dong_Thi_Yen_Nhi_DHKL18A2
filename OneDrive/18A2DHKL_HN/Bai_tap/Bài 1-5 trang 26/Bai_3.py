class PS:
    def __init__(self, tu_so, mau_so):
        self.tu_so=tu_so
        self.mau_so=mau_so

    def in_thong_tin(self):
        print(f"phân số: {self.tu_so}/{self.mau_so} ")
    def kiem_tra_tinh_hop_le(self):
        if self.mau_so != 0: 
            print(f"phan so  hop le")
           
        else: 
            print("phan so ko hop le")
           
   
print("Nhap phan so:")
tu_so=int(input("Nhap tử số: "))
mau_so=int(input("Nhập mẫu số: "))
phan_so=PS(tu_so,mau_so)
phan_so.in_thong_tin()
phan_so.kiem_tra_tinh_hop_le()
    
    




        
        
