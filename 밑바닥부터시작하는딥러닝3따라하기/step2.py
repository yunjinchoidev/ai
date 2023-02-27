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
    

import numpy as np

x = Variable(np.array(10))
f = Square()

# 어떻게 이것이 가능한걸까?
# 파이썬의 객체, 상속 원리에 대해서 알고 있어야 한다.
y = f(x)

print(type(y))
print(y.data)


