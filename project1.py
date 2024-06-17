import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)

user = eval(input('함수를 입력하세요 : '))

def f(x):
    return user

def f_prime(a, h=1e-6):
    return (f(a+h)-f(a))/h


plt.plot(x, f(x), color='red', label='function')
plt.plot(x, f_prime(x), color='blue', label='prime function')
plt.legend()
plt.grid()
plt.show()