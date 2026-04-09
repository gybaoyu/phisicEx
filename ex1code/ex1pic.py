import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 原始实验数据
I_B = np.array([0, 0.200, 0.283, 0.346, 0.400, 0.447, 0.490, 0.529, 0.566, 0.600, 0.663])
I_P = np.array([34.6, 31.0, 12.6,5.00, 2.20, 0.800, 0.200, 0.000,0.000, 0.000, 0.000])

# 常数 K
K = 22.1  # 单位: eV/A²

# 计算 E_k = K * I_B²
E_k = K * I_B**2
print(E_k)

# 计算微分分布数据
delta_I_P = abs(np.diff(I_P))  # 对I_P求差，对应相邻I_P值的差
delta_E_k = (E_k[:-1] + E_k[1:]) / 2  # 取相邻E_k的中间值作为横坐标

# 创建画布
plt.figure(figsize=(14, 6))

# 第一张图：累积分布曲线 (I_P vs E_k)
plt.subplot(1, 2, 1)
plt.plot(E_k, I_P, marker='o', linestyle='-', color='blue')
plt.xlabel('动能 $E_k$ (eV)')
plt.ylabel('阳极电流 $I_P$ (μA)')
plt.title('电子累积分布曲线')
plt.grid(True)

# 第二张图：微分分布曲线 (ΔI_P vs E_k)
plt.subplot(1, 2, 2)
plt.plot(delta_E_k, delta_I_P, marker='s', linestyle='-', color='red')
plt.xlabel('动能 $E_k$ (eV)')
plt.ylabel('电流差值 $\\Delta I_P$ (μA)')
plt.title('电子动能微分分布曲线')
plt.grid(True)

# 调整布局并显示
plt.tight_layout()
plt.show()

# 输出峰值位置和对应的动能，用于估算表面势垒
peak_index = np.argmax(delta_I_P)
peak_E_k = delta_E_k[peak_index]
print(f"微分分布曲线的峰值出现在动能: {peak_E_k:.3f} eV")

