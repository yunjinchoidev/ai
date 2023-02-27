import numpy as np

# 변수로 만들기.
class Variable:
    def __init__(self, data):
        self.data = data
    

# 함수 기본 베이스 라인
# 이것을 상속해서 변수를 함수 값에 넣는 클래스를 생성한다.
class Function:
    def __call__(self, input):
        x = input.data
        y = self.forward(x)
        output = Variable(y)
        self.input = input
        self.output = output
        return output
    
    def forward(self, x):
        raise NotImplementedError()
    

# 제곱 함수
class Square(Function):
    def forward(self, x):
        return x ** 2

# 익스포넨셜 함수
class Exp(Function):
    def forward(self, x):
        return np.exp(x)


# 미분을 한다.
# 미분의 정의 ? 극소분의 기울기
def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2*eps)


# 1>
# 제곱함수를 미분하는겨.
f = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f,x)
print(dy)


# 2> 
# 이번엔 함성함수를 미분해보자.
def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

x = Variable(np.array(0.5))

# 함성함수를 미분한겨.
dy = numerical_diff(f, x)
print(dy)
