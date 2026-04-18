import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号
# 原始数据
n = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
m = 20 * n  # g

single_up = np.array([-0.0057, 0.0178, 0.0418, 0.0656, 0.0895, 0.1134, 0.1370])
single_dn = np.array([-0.0059, 0.0176, 0.0417, 0.0654, 0.0893, 0.1132, 0.1370])

double_up = np.array([0.0051, 0.0467, 0.0956, 0.1440, 0.1926, 0.2414, 0.2893])
double_dn = np.array([0.0037, 0.0514, 0.0992, 0.1470, 0.1941, 0.2416, 0.2893])

full_up = np.array([0.0000, 0.0930, 0.1883, 0.2827, 0.3764, 0.4703, 0.5645])
full_dn = np.array([-0.0034, 0.0900, 0.1844, 0.2800, 0.3745, 0.4700, 0.5045])

single_avg = (single_up + single_dn) / 2
double_avg = (double_up + double_dn) / 2
full_avg = (full_up + full_dn) / 2

def fit_line(x, y):
    k, b = np.polyfit(x, y, 1)
    yhat = k * x + b
    r2 = 1 - np.sum((y - yhat)**2) / np.sum((y - y.mean())**2)
    return k, b, yhat, r2

k1, b1, y1, r21 = fit_line(m, single_avg)
k2, b2, y2, r22 = fit_line(m, double_avg)
k3, b3, y3, r23 = fit_line(m, full_avg)

plt.figure(figsize=(10, 7))
plt.plot(m, single_avg, 'o-', label=f'单臂平均  k={k1*1000:.3f} mV/g, R^2={r21:.5f}')
plt.plot(m, y1, '--', alpha=0.7)
plt.plot(m, double_avg, 's-', label=f'双臂平均  k={k2*1000:.3f} mV/g, R^2={r22:.5f}')
plt.plot(m, y2, '--', alpha=0.7)
plt.plot(m, full_avg, '^-', label=f'全臂平均  k={k3*1000:.3f} mV/g, R^2={r23:.5f}')
plt.plot(m, y3, '--', alpha=0.7)

plt.xlabel('质量 m (g)')
plt.ylabel('输出电压 U (V)')
plt.title('单臂/双臂/全臂电桥：输出电压-质量关系')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()

# 如需看上行与下行对比（例如全臂120g点）
plt.figure(figsize=(8, 5))
plt.plot(m, full_up, 'o-', label='全臂上行')
plt.plot(m, full_dn, 's-', label='全臂下行')
plt.xlabel('质量 m (g)')
plt.ylabel('输出电压 U (V)')
plt.title('全臂电桥上行/下行对比')
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()