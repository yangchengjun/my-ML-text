import torch
import numpy as np

#abs绝对值absolute
data = [-1,-2,1,2]
#将4bit的int型数据，存为32bit浮点型
tensor = torch.FloatTensor(data)


print(
    '\nabs',
    '\nnumpy:',np.abs(data),
    '\ntorch:',torch.abs(tensor),#torch只能处理浮点型
    #'\ntorchdata:',torch.abs(data),#TypeError: abs(): argument 'input' (position 1) must be Tensor, not list
)
#sin 三角函数

print(
    '\sin',
    '\nnumpy',np.sin(data),
    '\ntorch',torch.sin(tensor),
)

#mean 平均值

print(
    '\mean',
    '\nnumpy',np.mean(data),
    '\ntorch',torch.mean(tensor),
)
#add (addcdiv)
print(
    '\naddsin',
    '\nnumpy',np.add(data,np.sin(data)),
    '\ntorch',torch.add(tensor,tensor),
)
#ceil返回一个新的张量，其中包含输入元素的个数，大于或等于每个元素的最小整数,floor与它正好相反
apary = np.array(data)
print(
    '\nceil',
    '\nnumpyceil',np.ceil(torch.sin(tensor)),
    '\ntorchsin',torch.sin(tensor),
)
#clamp夹住输入范围内的所有元素[最小，最大]
print(
    '\nclamp',
    #'\nnumpyclamp',np.clamp(torch.sin(tensor)),
    '\ntensor',tensor,
    '\ntorchclamp',torch.clamp(tensor,-2,1),
)
#conj计算给定输入张量的元素级共轭
print(
    '\nconj',
    '\nnumpy',np.conj(data),
    '\ntorch',torch.conj(torch.sin(tensor)),
)