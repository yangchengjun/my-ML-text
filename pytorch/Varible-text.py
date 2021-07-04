import torch
from torch.autograd import Variable #Variable模块存在自动毕业中
#定义一个浮点变量
ts = torch.FloatTensor([[1,2],[3,4]])#gradients必须要浮点数
#将ts放到变量中，并设置需要计算梯度，参与误差反向传播
vb = Variable(ts,requires_grad =True)
T_out = torch.mean(ts*ts)
V_out = torch.mean(vb*vb)
V_out.backward()

print('tensor',ts,'\nvariable',vb)
print('tensor',T_out,'\nvariable',V_out)
print('vbgrad=',vb.grad)