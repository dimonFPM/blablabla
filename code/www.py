q = open("../ttt.txt", 'r')
for i in range(3):
    p = q.readline()
p = q.readlines()
print(p)
for i in range(len(p)):
    p[i] = float(p[i])
print("--------------------")
print(p)
q.close()
q = open("../rrr.txt", 'w')
a = ["agagag\n", "kklkjalfalfh\n", "kafihagh"]
q.writelines(a)
q.close()
# for i in range(len(p)):
#     p.insert(0)

# import numpy as np
#
# s = [i for i in np.arange(1, 10, 0.01)]
# print((s))


# import matplotlib.pyplot as plt
#
# x = [i for i in range(0, 10)]
# y = [i ** 2 for i in range(0, 10)]
# print(x)
# print(y)
# plt.figure("график 1")
# plt.title("cccc")
# plt.xlim(0, 10)
# plt.grid()
# plt.plot(x, y, label="график 1")
# plt.plot(y,x)
# plt.legend()
# plt.show()