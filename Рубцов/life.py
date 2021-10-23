import time
import tkinter as tk
from loguru import logger
import tkinter.messagebox as mbox


# def check_size(e_size: tk.Entry):
#     check_size_x = e_size.get()
#     if check_size_x.find("-") == 0:
#         x, *y = check_size_x
#         print()
#         if y.isnumeric():
#             print("это число")
#     pass
#     if check_size_x.isnumeric():
#         try:
#             size = int(e_size.get())
#             if size == 0 or size < 0:
#                 e_size.config(fg="red")
#                 logger.error("Введёное значение размерности равно 0 или меньше 0")
#                 # pass
#             else:
#                 e_size.config(fg="black")
#                 action(now_list)
#                 # pass
#         except:
#             logger.error("введённая размерность является isnumeric, но не int")
#             mbox.showerror("Ошибка", "Невозможно провести проверку введённого значения")
#     else:
#         logger.error("Введёное значение размерности не целое число")
#         e_size.config(fg="red")
#     # root.update()

def paint_grid(canvas: tk.Canvas, width_win: int, size: int):
    # описание
    if size > 0:  # проверка на ноль, size не может быть равным нулю
        shag = (width_win - width_win * 0.07) / size
        canvas.delete("line")
        canvas.delete("circle")
        for i in range(size - 1):  # от 0 до size
            canvas.create_line(0 + width_win * 0.003 + shag * (i + 1),
                               0 + width_win * 0.003,  # 2
                               0 + width_win * 0.003 + shag * (i + 1),
                               width_win - width_win * 0.069, tag="line")
        for i in range(size - 1):
            canvas.create_line(0 + width_win * 0.003,
                               0 + width_win * 0.003 + shag * (i + 1),
                               width_win - width_win * 0.069,
                               0 + width_win * 0.003 + shag * (i + 1), tag="line")
    else:
        mbox.showerror("Ошибка", "Размерность поля меньше 1")
        logger.error("Размерность поля не может быть меньше 1")


def paint_canvas(root: tk.Tk, size: int):
    # Отрисовка поля в процентах.Функция отрисовывает поле в процентах от разрешения экрана.
    # На вход подаётся экземпляр класса Tk.
    # Функция возвращает экземпляр класса Canvas.
    canvas_for_field = tk.Canvas(root, width=width_win - width_win * 0.07, height=width_win - width_win * 0.07,
                                 bg="white")
    canvas_for_field.pack(side=tk.LEFT, padx=width_win * 0.015, pady=width_win * 0.015)
    canvas_for_field.create_rectangle(0 + width_win * 0.003,
                                      0 + width_win * 0.003,
                                      width_win - width_win * 0.069,
                                      width_win - width_win * 0.069,
                                      outline='black')
    return canvas_for_field


def paint_circle(canvas: tk.Canvas, circle_tuple: tuple):
    # Отрисовка кругов всего массива. Отрисовывает круги на Canvas согласно списку.
    # На вход получает экземляр класса  Canvas и список, элементы которого требуется отрисовать. Ничего не воозвращает.
    canvas.delete("circle")
    shag = (width_win - width_win * 0.07) / int(size.get())#######################передаь ширину и размер
    for i in range(len(circle_tuple)):
        for j in range(len(circle_tuple)):
            if circle_tuple[i][j][0] == 1:
                canvas.create_oval(shag * j + width_win * 0.0065,
                                   shag * i + width_win * 0.0065,
                                   shag * j + shag,
                                   shag * i + shag,
                                   fill="red",
                                   tag="circle")


def sosedi_chek(i: int, j: int, list1: list):
    # место для описания

    x = len(list1[0]) - 1
    if i == 0:
        if j == 0:  # угол1
            summa = sum((list1[x][x][0], list1[x][j][0],
                         list1[x][j + 1][0], list1[i][x][0], list1[i][j + 1][0],
                         list1[i + 1][x][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        elif j == x:  # угол 2
            summa = sum((list1[x][j - 1][0], list1[x][j][0], list1[0][x][0],
                         list1[i][j - 1][0], list1[0][0][0], list1[i + 1][j - 1][0], list1[i + 1][j][0],
                         list1[i + 1][0][0]))
        elif j != 0 and j != x:  # сторона при i=0
            summa = sum((list1[x][j - 1][0], list1[x][j][0], list1[x][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
    elif i == x:
        if j == 0:  # угол 3
            summa = sum((list1[i - 1][x][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][x][0], list1[i][j + 1][0], list1[0][x][0],
                         list1[0][j][0], list1[0][j + 1][0]))
        elif j == x:  # угол 4
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][0][0],
                         list1[i][j - 1][0], list1[i][0][0],
                         list1[0][j - 1][0], list1[0][j][0], list1[0][0][0]))
        elif j != 0 and j != x:  # сторона при i=x
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[0][j - 1][0], list1[0][j][0], list1[0][j + 1][0]))
    elif i != 0 and i != x:
        if j == 0:  # строна при j=0
            summa = sum((list1[i - 1][x][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][x][0], list1[i][j + 1][0],
                         list1[i + 1][x][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        elif j == x:  # сторона при j=x
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][0][0],
                         list1[i][j - 1][0], list1[i][0][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][0][0]))
        else:
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
    match summa:
        case 0:
            return 0
        case 1:
            return 0
        case 2:
            if list1[i][j][0]:
                return 1
            else:
                return 0
        case 3:
            return 1
        case _:
            return 0


def check_size(*args):
    x = e_size.get()
    if x != "":
        if x.isnumeric():
            if int(e_size.get()) > 0:
                size = int(e_size.get())
                e_size.config(fg='black')
                logger.info(f"size={int(e_size.get())}")
                paint_grid(canvas, width_win, size)
            else:
                e_size.config(fg='red')
        else:
            e_size.config(fg='red')
            logger.info("e_size либо отрицательное либо текстовое значение")
    else:
        logger.info("e_size пустое поле")


@logger.catch()
def action(now_list: tuple):
    shag = (width_win - width_win * 0.07) / int(size.get())#######################передаь ширину и размер
    future_list = now_list
    future_list = list(future_list)
    for i in range(len(future_list)):
        future_list[i] = list(future_list[i])
        for j in range(len(future_list)):
            future_list[i][j] = list(future_list[i][j])
    logger.info(future_list)  # future_list - список
    logger.info(f"{type(future_list)=}")
    k = 0
    logger.info(f"{len(now_list)=}\n{len(future_list)=}")
    while True:
        logger.info(f"{k=}")
        for i in range(len(future_list)):
            for j in range(len(future_list)):
                future_list[i][j][0] = sosedi_chek(i, j, now_list)
                logger.info(f"{i=} {j=}")
        k += 1
        # if now_list == future_list:#############################################   не сработает так как один элемент массив, а другой кортеж
        #     logger.info("конфигурации совпали, изменений больше небудет")
        #     break
        paint_circle(canvas, tuple(future_list))
        canvas.update()
        time.sleep(0.5)

        if k == 10:
            logger.info("финальное k={}".format(k))
            break

        # кортеж в список
        now_list = list(now_list)
        for i in range(len(now_list)):
            now_list[i] = list(now_list[i])
            for j in range(len(now_list)):
                now_list[i][j] = list(now_list[i][j])

        now_list = future_list
        ####

        # список в кортеж
        for i in range(len(now_list)):
            for j in range(len(now_list)):
                now_list[i][j] = tuple(now_list[i][j])
            now_list[i] = tuple(now_list[i])
        now_list = tuple(now_list)

        for i in range(len(future_list)):
            future_list[i] = list(future_list[i])
            for j in range(len(future_list)):
                future_list[i][j] = list(future_list[i][j])

        logger.info(f"{len(now_list)=}\n{len(future_list)=}")
        logger.info(f"{future_list=}")
        logger.info(f"{now_list=}")
        #####


# def init():


# region установка параметров окна приложения
logger.add("log_life.log", level="DEBUG", format="{time} {level} {message}")
# logger.remove()
root = tk.Tk()
root.title("стартовое окно")
width_win, height_win = map(int, (root.winfo_screenwidth() * 0.5,
                                  root.winfo_screenheight() * 0.5))  # задание размеров окна приложения
root.geometry(f"{int(width_win * 1.5)}x{width_win}+0+0")
root.resizable(False, False)

# endregion

# region установка и проверка размерности(size)
size = 0  # int(input("введите размерность сетки: "))  # размерность сетки для поля
# if size > 0:  # проверка на 0
#     shag = (width_win - width_win * 0.07) / size
# else:
#     logger.error(f"Размерность сетки равна {size=}, невозможно расчитать шаг сетки.")
#     mbox.showerror("Ошибка", "Невозможно рассчитать шаг. Размернось поля не может быть равной нулю")
#     exit()

# endregion

# region заполнение тестового массива
now_list = [[[1], [1], [0], [0], [0], [0], [0], [0]],
            [[1], [1], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [0], [0], [0], [0], [0]],
            [[0], [0], [0], [1], [1], [0], [0], [0]],
            [[0], [0], [1], [1], [0], [0], [0], [0]],
            [[1], [0], [0], [0], [0], [1], [1], [0]],
            [[0], [1], [0], [0], [0], [0], [1], [0]],
            [[0], [1], [1], [0], [0], [0], [1], [0]]]

######трёх-мерный список в трёх-мерный кортеж
for i in range(len(now_list)):
    for j in range(len(now_list)):
        now_list[i][j] = tuple(now_list[i][j])
    now_list[i] = tuple(now_list[i])
now_list = tuple(now_list)
# endregion

# region удалить
# # print("list1=", now_list)
# future_list = now_list
# # print("list2=", future_list)
#
# #####трёх-мерный кортеж в трёх-мерный список
# future_list = list(future_list)
# for i in range(len(future_list)):
#     future_list[i] = list(future_list[i])
#     for j in range(len(future_list)):
#         future_list[i][j] = list(future_list[i][j])
# ########удалить
# endregion

# region Canvas и  Frame
canvas = paint_canvas(root, size)
# paint_grid(canvas, width_win, size)
fr = tk.Frame(root)
# endregion

# region Button
b_action = tk.Button(fr, text="action", command=lambda: action(now_list), width=int(width_win * 0.03125))
b_cancel = tk.Button(fr, text="cancel", width=int(width_win * 0.03125))
b_start_config = tk.Button(fr, text="начальное состояние", width=int(width_win * 0.03125),
                           command=lambda: paint_circle(canvas, now_list))
# endregion

# region Label
l_size = tk.Label(fr, text="Размерность поля:")
# endregion

# region Entry
size = tk.StringVar()
size.trace('w', check_size)
e_size = tk.Entry(fr, justify=tk.CENTER, fg="black", textvariable=size)
# e_size.insert(0, "8")  #####удалить
# endregion

# region Pack
fr.pack(side=tk.LEFT)
l_size.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
e_size.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_action.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_cancel.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
b_start_config.pack(side=tk.TOP, padx=int(width_win * 0.015625), pady=int(width_win * 0.00781))
# endregion


# paint_circle(canvas, now_list)  # начальная конфигурация
root.mainloop()
