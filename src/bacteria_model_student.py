import numpy as np
import matplotlib.pyplot as plt

class BacteriaModel:
    # 定义W(t)函数
 
    def W(t, A, tau):
        return A * (np.exp(-t / tau) - 1 + t / tau)

    # 定义V(t)函数
    def V(t, tau):
        return 1 - np.exp(-t / tau)

    # 读取实验数据
    def load_bacteria_data(filename):
        try:
            data = np.loadtxt('g194novickB.txt',delimiter=',')
            return data['time'], data['response']
        except:
            return np.loadtxt('g194novickB.txt', delimiter=',', unpack=True)
        t_data = data[:, 0]
        V_data = data[:, 1]
        # 丢弃所有时间值大于10小时的数据
        mask = t_data <= 10
        t_data = t_data[mask]
        V_data = V_data[mask]
        return t_data, V_data

# 定义参数
t = np.linspace(0, 2, 500)

# a. 选择A = 1, τ = 1，并绘制0 < t < 2的W(t)
A1, tau1 = 1, 1
W1 = BacteriaModel.W(t, A1, tau1)

plt.plot(t, W1, label=f'A={A1}, τ={tau1}', linestyle='-', color='blue')

# b. 使用不同的τ和A值制作几个数组W1、W2、W3等，并在同一图上同时绘制它们
A2, tau2 = 2, 0.5
W2 = BacteriaModel.W(t, A2, tau2)
plt.plot(t, W2, label=f'A={A2}, τ={tau2}', linestyle='--', color='red')

A3, tau3 = 0.5, 2
W3 = BacteriaModel.W(t, A3, tau3)
plt.plot(t, W3, label=f'A={A3}, τ={tau3}', linestyle='-.', color='green')

# 更改线条的颜色和样式（实线、虚线等）
# 已在上面代码中实现

plt.legend()
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Novick-Weiner')
plt.grid(True)

# 显示图形
plt.show()

# 读取实验数据
t_data, V_data = BacteriaModel.load_bacteria_data('data/g149novickB.txt')

# 绘制V(t)和实验数据点
tau_values = [0.5, 1, 2]
for tau in tau_values:
    V_model = BacteriaModel.V(t, tau)
    plt.plot(t, V_model, label=f'τ={tau}')

plt.scatter(t_data, V_data, color='black', marker='o', label='data')

plt.legend()
plt.xlabel('t')
plt.ylabel('V(t)')
plt.title('Experimental Data')
plt.grid(True)

# 显示图形
plt.show()

