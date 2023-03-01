class Variable:
    def __init__(self, data):
        self.data = data

class Function:

    # call 메소드는 파이썬의 특수 메소드다. f= Fucntion()  으로 인스턴스를 만들고 f(x) 형태로 call 메소드를 바로 호출할 수 있다.
    def __call__(self, input): 
        x = input.data

        # 클래스의 forword 함수를 사용하겠다.
        y = self.forward(x)
        output = Variable(y)
        return output
    
    def forward(self, in_data):
        raise NotImplementedError()
    
class Square(Function):
    def forward(self, x):
        return x ** 2
    
class Exp(Function):
    def forward(self, x):
        return np.exp(x)
    

import numpy as np

A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))

# 어떻게 이것이 가능한가?
# 설명해보라 ! 
a = A(x)
b = B(a)
y = C(b)

print(y.data)

# 이로써 우리는 합성함수를 구현하게 되었다.

