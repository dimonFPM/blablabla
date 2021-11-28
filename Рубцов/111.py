# def paint_canvas(root, size):  # отрисовка поля
#     canvas_for_field = tk.Canvas(root, width=width_win - 49, height=width_win - 49, bg="white")
#     canvas_for_field.pack(side=tk.TOP, padx=10, pady=10)
#     canvas_for_field.create_rectangle(2, 2, width_win - 48, width_win - 48, outline='black')
#     for i in range(size - 1):  # от 0 до size
#         canvas_for_field.create_line(2 + shag * (i + 1), 2, 2 + shag * (i + 1), width_win - 48)
#     for i in range(size - 1):
#         canvas_for_field.create_line(2, 2 + shag * (i + 1), width_win - 48, 2 + shag * (i + 1))
#     return canvas_for_field
#
#
# def paint_circle(canvas, circle_tuple):#отрисовка кругов всего массива
#     canvas.delete("circle")
#     circle_list = list(circle_tuple)
#     for i in range(len(circle_list)):
#         for j in range(len(circle_list)):
#             if circle_list[i][j][0] == 1:
#                 canvas.create_oval(shag * i + 4, shag * j + 4, shag * i + shag, shag * j + shag, fill="red",
#                                    tag="circle")


# now_list = []
# for i in range(5):
#     now_list.append([])
#     for j in range(5):
#         now_list[i].append([])
# print(now_list)

# now_list = [[[] for _ in range(5)] for _ in range(5)]
# print(now_list)
# import random
# import tkinter.messagebox as mbox
#
# from loguru import logger
#
#
# def list_generation(e_size: int, procent_zapolnenia=50) -> tuple:
#     if True:  # e_size["fg"] == "black":
#         size = int(e_size)  # int(e_size.get())
#         count_element = size * size
#         now_list = [[[0] for _ in range(size)] for _ in range(size)]
#         ####заполенение случайных полей
#         logger.info(f"{count_element=}\n{procent_zapolnenia=}")
#         logger.info(int(count_element * (procent_zapolnenia / 100)))
#         k = 0
#         while k <= int(count_element * (procent_zapolnenia / 100)):
#             i = random.randint(0, size - 1)
#             j = random.randint(0, size - 1)
#             # logger.info(f"{i=} {j=}")
#             if now_list[i][j][0] == 0:
#                 now_list[i][j][0] = 1
#                 k += 1
#         ####
#         for i in range(len(now_list)):
#             for j in range(len(now_list)):
#                 now_list[i][j] = tuple(now_list[i][j])  # добавить вложенный список
#             now_list[i] = tuple(now_list[i])
#         now_list = tuple(now_list)
#         logger.info(f"{type(now_list)=}")
#         # paint_circle(canvas, now_list)
#         return now_list
#     else:
#         mbox.showerror("Ошибка", "Размерность поля не целое число")
#         logger.error("размерность поля не целое число")
#
#
# a = list_generation(5)
# print(*a, sep="\n")
# def a():
#     return 4, 5
#
#
# x, y = a()
# print(x, y)
#
# a = [[j for j in range(5)] for i in range(5)]
# print(*a, sep="\n")
#
# print(a[-1][-1])
# now_list = (((1,), (0,), (0,), (0,), (1,)),
#             ((0,), (0,), (1,), (1,), (0,)),
#             ((0,), (1,), (1,), (0,), (0,)),
#             ((0,), (1,), (1,), (1,), (0,)),
#             ((1,), (0,), (0,), (0,), (1,)))
# logger.info(f"сгенерированный список")
# for i in range(len(now_list)):
#     logger.info(now_list[i])
# import random
#
# size = 3
# #######
# a = [[[0] for j in range(size + 2)] for i in range(size + 2)]
# for i in range(1, len(a) - 1):
#     for j in range(1, len(a) - 1):
#         a[i][j] = random.randint(0, 1)
#
# for j in range(1, len(a) - 1):
#     a[0][j] = a[len(a) - 2][j]
#     a[len(a) - 1][j] = a[1][j]
#
# for i in range(0, len(a)):
#     a[i][0] = a[i][len(a) - 2]
#     a[i][len(a) - 1] = a[i][1]
# ######3
# print(*a, sep="\n")
#
#
#
# for i in range(1, len(a) - 1):
#     for j in range(1, len(a) - 1):
#         summa = sum((a[i - 1][j - 1], a[i - 1][j], a[i - 1][j + 1],
#                     a[i][j - 1], a[i][j + 1],
#                     a[i + 1][j - 1], a[i + 1][j], a[i + 1][j + 1]))
#         print(f"{i=} {j=} {summa=}")
#

# def f2(func):
#     def ff(x, y):
#         print("сейчас напечатается что-то")
#         func(x, y)
#         print("а это напечатается после неё")
#     return ff
#
# @f2
# def f1(x, y):
#     print(f"{x+y=}")
#
#
# x, y, *_ = map(int, input("введите два числа:\n").split())
# f1(x, y)
# print(_)


# match k:
#     case 0:
#         future_list[i][j][2] = "#EB1101"
#     case 1:
#         future_list[i][j][2] = "#EB2413"
#     case 2:
#         future_list[i][j][2] = "#EB3323"
#     case 3:
#         future_list[i][j][2] = "#EB4032"
#     case 4:
#         future_list[i][j][2] = "#EB5547"
#     case 5:
#         future_list[i][j][2] = "#EB6459"
#     case 6:
#         future_list[i][j][2] = "#EB7D74"
#     case 7:
#         future_list[i][j][2] = "#EB9B94"
#     case 8:
#         future_list[i][j][2] = "#EBB7B5"
#     case 9:
#         future_list[i][j][2] = "#EBD0D1"
# import os
# try:
#     os.mkdir("новая папка")
# except FileExistsError:
#     print("данная папка уже существует")
# a = map(int, (4.5, 6.8))
# print(a)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # a = [i for i in a if i > 5]
# a = list(filter(lambda x: x > 5, a))
# print(a)
import random
import tkinter as tk

# def new_window():
#     # root = tk.Toplevel()
#     root.title("второстепенное окно")
#     root.geometry("200x200+100+100")
#     b.pack_forget()
#     tk.Label(root, text="запись в новом окне").pack(side=tk.TOP)
#     # root.destroy()
#
#
# root = tk.Tk()
# root.title("главное окно")
# root.geometry("200x200+100+100")
# l = tk.Label(root, text="нажми на эту кнопку")
# l.pack(side=tk.TOP)
# b = tk.Button(root, text="новое окно", command=new_window)
# b.pack(side=tk.TOP)
#
# root.mainloop()

# l_age,l_size,e_size,l_nomer_age,e_nomer_age,l_procent_zapolnenia,e_procent_zapolnenia,b_action,b_cancel,b_start_config,b_generation,b_openfile,b_savefile,cbox_death

# a = [10, 10]
#
#
# def f():
#     s = [1, 2, *a]
#     print(s)
#
#
# f()
# match (1, 1, 3, 1):
#     case 1, 1, 1, 1:
#         print("1,1,1,1")
#     case 1, 1, 0, 1:
#         print("1,1,0,1")
#     case _:
#         print("нет подходящих вариантов")
#
# for i in range(0,10,2):
#     print(i)
# import random

# a = [[random.randint(0, 10) for j in range(10)] for i in range(10)]
# print(*a,sep="\n")
#
# print("\n",a[-1])

#
# a = [i for i in range(2, 11, 2)]
# print(a)

import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x, y = np.mgrid[0:5:1, 0:5:1]
print(x)
print(y)

# y = np.array([i for i in range(10)])
z = [[0 for _ in range(10)] for _ in range(10)]
z = [[0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 1, 1, 0],
     [0, 1, 1, 2, 0],
     [0, 0, 0, 0, 0]]

z = np.array(z)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
# ax.legend()
ax.plot_surface(x, y, z)
plt.show()
