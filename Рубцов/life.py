import tkinter as tk

root = tk.Tk()
root.title("стартовое окно")
width_win, height_win = map(int, (root.winfo_screenwidth() * 0.5,
                                  root.winfo_screenheight() * 0.5))  # задание размеров окна приложения
root.geometry(f"{width_win}x{width_win}+0+0")
root.resizable(False, False)

size = 50  # int(input("введите размерность сетки: "))  # размерность сетки для поля
shag = (width_win - width_win * 0.07) / size


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
    circle_list = list(circle_tuple)
    for i in range(len(circle_list)):
        for j in range(len(circle_list)):
            if circle_list[i][j][0] == 1:
                canvas.create_oval(shag * i + width_win * 0.0065,
                                   shag * j + width_win * 0.0065,
                                   shag * i + shag,
                                   shag * j + shag,
                                   fill="red",
                                   tag="circle")


def sosedi_chek(i: int, j: int, list1: list):
    # место для описания
    x = len(list1) - 1
    match i, j:
        # углы
        case 0, 0:
            summa = sum((list1[len(list1) - 1][len(list1) - 1][0], list1[len(list1) - 1][j][0],
                         list1[len(list1) - 1][j + 1][0], list1[i][len(list1) - 1][0], list1[i - 1][j - 1][0],
                         list1[i + 1][len(list1) - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        case 0, x:
            summa = sum((list1[len(list1) - 1][j - 1][0], list1[len(list1) - 1][j][0], list1[0][len(list1) - 1][0],
                         list1[i][j - 1][0], list1[i][0][0], list1[i + 1][j - 1][0], list1[i + 1][j][0],
                         list1[i + 1][0][0]))

        case x, 0:
            summa = sum((list1[i - 1][len(list1) - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                         list1[i][len(list1) - 1][0], list1[i - 1][j - 1][0],
                         list1[0][len(list1) - 1][0], list1[0][j][0], list1[0][j + 1][0]))
        case x, x:
            summa = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][0][0],
                         list1[i][j - 1][0], list1[i - 1][0][0],
                         list1[0][j - 1][0], list1[0][j][0], list1[0][0][0]))
        # стороны
        case 0, j:
            summa = sum((list1[x][j - 1][0], list1[x][j][0], list1[x][j + 1][0],
                         list1[i][j - 1][0], list1[i][j + 1][0],
                         list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        case x, j:
            summma = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                          list1[i][j - 1][0], list1[i][j + 1][0],
                          list1[0][j - 1][0], list1[0][j][0], list1[0][j + 1][0]))
        case i, 0:
            summma = sum((list1[i - 1][x][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                          list1[i][x][0], list1[i][j + 1][0],
                          list1[i + 1][x][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        case i, x:
            summma = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
                          list1[i][j - 1][0], list1[i][j + 1][0],
                          list1[i + 1][j - 1][0], list1[i + 1][j][0], list1[i + 1][j + 1][0]))
        # остальные элементы
        case _:
            summma = sum((list1[i - 1][j - 1][0], list1[i - 1][j][0], list1[i - 1][j + 1][0],
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


# создание тестового массива
now_list = [[[0] for _ in range(size)] for _ in range(size)]  # генератор массива, потом надо заменить на список классов
for i in range(len(now_list)):
    print(now_list[i])
print("\n")
#############################


# заполнение тестового массива
l = (0, 1, 4, 7, 3, 9, 46, 5, 43, 12, 7)
l2 = (0, 1, 6, 3, 7, 5, 9, 34, 28, 6, 9)
for i in range(len(l)):
    now_list[l[i]][l2[i]][0] = 1
for i in range(len(now_list)):
    print(now_list[i])
# #############################

canvas = paint_canvas(root, size)
paint_circle(canvas, tuple(now_list))

future_list = [[[] for _ in range(size)] for _ in range(size)]  ###############3
# алгоритм
while True:
    # future_list.clear()
    for i in range(len(now_list)):
        for j in range(len(now_list)):
            future_list[i][j][0] = sosedi_chek(i, j, now_list)
    if now_list == future_list:
        break
    paint_circle(canvas, tuple(future_list))
#########
root.mainloop()
