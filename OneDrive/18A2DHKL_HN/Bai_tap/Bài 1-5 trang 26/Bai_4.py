class Stack:
    def __init__(self, max_size):
        self.max_size = max_size     
        self.stack = []          

    def __del__(self):
        print("Ngăn xếp đã hủy")

    def push(self, value: float):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm!")
        else:
            self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy!")
            return None
        value = self.stack.pop()
        print(f"Đã pop {value}")
        return value

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) >= self.max_size

    def display(self):
        print("Ngăn xếp:", self.stack)



sl = int(input("Nhập số phần tử tối đa của ngăn xếp: "))
ngan_xep = Stack(sl)

print(" Nhập các số thực vào ngăn xếp")
for i in range(sl):
    x = float(input(f"Số thực thứ {i+1}: "))
    ngan_xep.push(x)

ngan_xep.display()


print("kiem tra ngan xep  ")
ngan_xep.push(99.9)   


print("kiem tra ngan xep ")
for i in range(sl+1):   
    ngan_xep.pop()
ngan_xep.display()
