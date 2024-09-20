import math
import statistics as sts
txt_3 = ('''0.19 0.25 0.26 0.26 0.28 0.31 0.39 0.42 0.44 0.45
0.48 0.53 0.54 0.57 0.66 0.69 0.70 0.72 0.73 0.79
0.83 0.85 0.87 0.90 0.91 0.94 0.96 0.99 1.01 1.02
1.02 1.03 1.05 1.07 1.13 1.13 1.14 1.20 1.22 1.27
1.28 1.30 1.34 1.34 1.37 1.39 1.40 1.43 1.43 1.46
1.49 1.50 1.51 1.53 1.54 1.56 1.56 1.57 1.60 1.60
1.61 1.62 1.62 1.62 1.63 1.64 1.66 1.67 1.70 1.71
1.71 1.71 1.72 1.73 1.73 1.74 1.75 1.76 1.77 1.80
1.81 1.84 1.85 1.85 1.86 1.87 1.87 1.88 1.90 1.91
1.91 1.92 1.92 1.93 1.93 1.93 1.94 1.95 1.98 1.99''')
txt_x = ('''16 18 22 20 17 25 21 23 24 31 27 28 30 27 28''')
txt_y = ('''19 17 18 23 20 21 24 18 18 25 29 24 24 23 24''')
txt_3 = txt_3.split()
txt_x=txt_x.split()
txt_y=txt_y.split()
for i in range(len(txt_x)):
    txt_x[i] = int(txt_x[i])
for i in range(len(txt_y)):
    txt_y[i] = int(txt_y[i])
for i in range(len(txt_3)):
    txt_3[i] = float(txt_3[i])




txt = txt_x

print(f'Sum: {sum(txt)}')
print(f'Mean: {sum(txt)/len(txt)}')
print(f'Mean again: {sts.mean(txt)}')
print(f'Var: {sts.variance(txt)}')
print(f'Std Dev: {sts.stdev(txt)}')
print(f'Covariance: {sts.covariance(txt_x,txt_y)}')
print(f'Coeff of corr: {sts.correlation(txt_x,txt_y)}')
print(f'Linear regression: {sts.linear_regression(txt_x,txt_y)}')

