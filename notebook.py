# %%
from tinygrad.nn import Conv2d, Linear


class TestModel:
    def __init__(self):
        self.l1 = Conv2d(3, 3, 3)
        # self.l2 = Linear(2700, 10)

    def __call__(self, x):
        return self.l1(x)


# %%
import numpy as np


from tinygrad.tensor import Tensor
from tinygrad.jit import TinyJit
from tinygrad.nn import Conv2d, Linear


@TinyJit
def jit(x):
    m = TestModel()
    outputs = m(x)
    print(outputs.realize().numpy())

add_result = Tensor([2]) + Tensor([3])


#%%

from tinygrad.ops import Device
from tinygrad.tensor import Tensor
from tinygrad.helpers import prod

result = Tensor(2).realize() + Tensor(3).realize()
result.lazydata.realized = Device[Device.DEFAULT].buffer(prod(result.shape), result.dtype)

# use the real Linearizer to linearize 2+3
from tinygrad.codegen.linearizer import Linearizer, LinearizerOptions
linearizer = Linearizer(result.lazydata.op, result.lazydata, LinearizerOptions())
linearizer.linearize()

# print the uops
for uop in linearizer.uops: print(uop)

# TODO: feed into clang renderer