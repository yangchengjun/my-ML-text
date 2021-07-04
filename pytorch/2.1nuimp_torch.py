import torch
import numpy as np
#tensor 张量，array数组
np_data = np.arange(6).reshape((2,3))
#将一个数组类型的数据转化为张量
torch_data = torch.from_numpy(np_data)
#变回来
tensor2array = torch_data.numpy()

print('\nnumpy',np_data,
      '\ntorch',torch_data,
      '\ntensor2array',tensor2array,
      )