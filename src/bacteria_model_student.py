import numpy as np
import matplotlib.pyplot as plt

# 定义W(t)函数
def W(t, A, tau):
    return A * (np.exp(-t / tau) - 1 + t / tau)

# 定义参数
t = np.linspace(0, 2, 500)

# a. 选择A = 1, τ = 1，并绘制0 < t < 2的W(t)
A1, tau1 = 1, 1
W1 = W(t, A1, tau1)

plt.plot(t, W1, label=f'A={A1}, τ={tau1}', linestyle='-', color='blue')

# b. 使用不同的τ和A值制作几个数组W1、W2、W3等，并在同一图上同时绘制它们
A2, tau2 = 2, 0.5
W2 = W(t, A2, tau2)
plt.plot(t, W2, label=f'A={A2}, τ={tau2}', linestyle='--', color='red')

A3, tau3 = 0.5, 2
W3 = W(t, A3, tau3)
plt.plot(t, W3, label=f'A={A3}, τ={tau3}', linestyle='-.', color='green')

# c. 更改线条的颜色和样式（实线、虚线等）
# 已在上面代码中实现

# d. 添加图例帮助潜在读者区分曲线。探索可用的其他图选项。
plt.legend()
plt.xlabel('t')
plt.ylabel('W(t)')
plt.title('Novick-Weiner')
plt.grid(True)

# 显示图形
plt.show()
class BacteriaModel:
    def __init__(self, A, tau):
        self.A = A
        self.tau = tau

    def v_model(self, t):
        return 1 - np.exp(-t/self.tau)

    def w_model(self, t):
        return self.A * (np.exp(-t/self.tau) - 1 + t/self.tau)

    def plot_models(self, t):
        v = self.v_model(t)
        w = self.w_model(t)
        
        plt.plot(t, v, label='V(t)')
        plt.plot(t, w, label='W(t)')
        plt.xlabel('Time')
        plt.ylabel('Response')
        plt.title('Bacteria Growth Models')
        plt.legend()
        plt.show()

def load_bacteria_data(filepath):
    try:
        data = np.loadtxt(filepath,delimiter=',')
        return data['time'], data['response']
    except:
        return np.loadtxt(filepath, delimiter=',', unpack=True)

def main():
    # 初始化模型参数
    model = BacteriaModel(A=1.0, tau=2.0)
    
    # 生成时间序列
    t = np.linspace(0, 10, 100)
    
    # 绘制模型曲线
    model.plot_models(t)
    
    # 加载实验数据
    time_data, response_data = load_bacteria_data('data/g149novickA.txt')
    
    # 绘制实验数据
    plt.scatter(time_data, response_data, label='Experimental Data')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()

