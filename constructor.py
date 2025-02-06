class Mobile:
    def __init__(self, Brand, Battery, Ram, Camera, Price):
        self.Brand = Brand
        self.Battery = Battery
        self.Ram = Ram
        self.Camera = Camera
        self.Price = Price

    def display(self):
        print("Brand : ", self.Brand)
        print("Battery : ", self.Battery)
        print("Ram : ", self.Ram)
        print("Camera : ", self.Camera)
        print("Price : ", self.Price)

obj = Mobile("Apple",'4000mah', '8gb', '48mp', 55000)
obj.display()
print(" ")
obj = Mobile("Google Pixel",'4000mah', '8gb', '48mp', 55000)
obj.display()