# ploymorphism : When the same operator is allowed to have different meaning according to the
# operator overloadbing
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showComplex(self):
        print(self.real, "i +", self.img,"j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)

n1 = Complex(3,18)
n1.showComplex() 

n2 = Complex(4,10)
n2.showComplex() 

# n3 = n1.addComplex(n2)
# n3.showComplex()

# n3 = n1 + n2
# n3.showComplex()

n3 = n1-n2
n3.showComplex()