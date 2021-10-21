import time
import tkinter as tk
from loguru import logger

# logger.remove()
root = tk.Tk()
root.title("стартовое окно")
width_win, height_win = map(int, (root.winfo_screenwidth() * 0.5,
                                  root.winfo_screenheight() * 0.5))  # задание размеров окна приложения
root.geometry(f"{width_win}x{width_win}+0+0")
root.resizable(False, False)

size = 8  # int(input("введите размерность сетки: "))  # размерность сетки для поля
shag = (width_win - width_win * 0.07) / size


def paint_canvas(root: tk.Tk, size: int):
    # Отрисовка поля в процентах.Функция отрисовывает поле в процентах от разрешения экрана.
    # На вход подаётся экземпляр класса Tk и размер отисывываемой сетки.
    # Функция возвращает экземпляр класса Canvas.
    canvas_for_field = tk.Canvas(root, width=width_win - width_win * 0.07, height=width_win - width_win * 0.07,
                                 bg="white")
    canvas_for_field.pack(side=tk.TOP, padx=width_win * 0.015, pady=width_win * 0.015)
    canvas_for_field.create_rectangle(0 + width_win * 0.003,
                                      0 + width_win * 0.003,
                                      width_win - width_win * 0.069,
                                      width_win - width_win * 0.069,
                                      outline='black')
    for i in range(size - 1):  # от 0 до size
        canvas_for_field.create_line(0 + width_win * 0.003 + shag * (i + 1),
                                     0 + width_win * 0.003,  # 2
                                     0 + width_win * 0.003 + shag * (i + 1),
                                     width_win - width_win * 0.069)
    for i in range(size - 1):
        canvas_for_field.create_line(0 + width_win * 0.003,
                                     0 + width_win * 0.003 + shag * (i + 1),
                                     width_win - width_win * 0.069,
                                     0 + width_win * 0.003 + shag * (i + 1))
    return canvas_for_field


def paint_circle(canvas: tk.Canvas, circle_tuple: tuple):
    # Отрисовка кругов всего массива. Отрисовывает круги на Canvas согласно списку.
    # На вход получает экземляр класса  Canvas и список, элементы которого требуется отрисовать. Ничего не воозвращает.
    canvas.delete("circle")
    # circle_list = list(circle_tuple)
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


@logger.catch()
def action(now_list: tuple):
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
        root.update_idletasks()
        root.after(1000)

        if k == 1:
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
        #####3


# def init():


# заполнение тестового массива
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
########

# print("list1=", now_list)
future_list = now_list
# print("list2=", future_list)

#####трёх-мерный кортеж в трёх-мерный список
future_list = list(future_list)
for i in range(len(future_list)):
    future_list[i] = list(future_list[i])
    for j in range(len(future_list)):
        future_list[i][j] = list(future_list[i][j])
########

canvas = paint_canvas(root, size)
paint_circle(canvas, now_list)
action(now_list)

root.mainloop()
