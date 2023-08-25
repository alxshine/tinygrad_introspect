# %%
from tinygrad.nn import Conv2d, Linear


class TestModel:
    def __init__(self):
        self.l1 = Conv2d(3, 3, 3)
        self.l2 = Linear(2700, 10)

    def __call__(self, x):
        x = self.l1(x)
        x = x.relu()
        x = x.flatten()
        x = self.l2(x)

        return x


# %%
import numpy as np


from tinygrad.tensor import Tensor
from tinygrad.jit import TinyJit

@TinyJit
def jit(x):
    m = TestModel()
    outputs = m(x)
    print(outputs.realize().numpy())

np.random.seed(1337)
inputs = np.random.randn(1, 3, 32, 32)
input_tensor = Tensor(inputs)
    
jit(input_tensor)   