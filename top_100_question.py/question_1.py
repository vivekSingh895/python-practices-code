import numpy as np
import matplotlib.pyplot as plt

a = np.random.randint(10,50,5)
b = np.array([10000,30000,5000,12000,50000])
x = plt.plot(a,b, color = "red",marker = "o")
plt.title("normal data")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid("x axis")
plt.show()