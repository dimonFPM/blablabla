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


def paint_canvas(root, size):  # отрисовка поля
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


def paint_circle(canvas, circle_tuple):
    canvas.delete("circle")
    circle_list = list(circle_tuple)
    for i in range(len(circle_list)):
        for j in range(len(circle_list)):
            if circle_list[i][j][0] == 1:
                canvas.create_oval(shag * i + 4, shag * j + 4, shag * i + shag, shag * j + shag, fill="red",
                                   tag="circle")


# создание тестового массива
list1 = [[[0] for i in range(size)] for t in
         range(size)]  # генератор массива, потом надо заменить на список классов
for i in range(len(list1)):
    print(list1[i])
print("\n")
#############################


# заполнение тестового массива
# l = (0, 1, 4, 7, 3, 9, 46, 5, 43, 12, 7)
# l2 = (0, 1, 6, 3, 7, 5, 9, 34, 28, 6, 9)
# for i in range(len(l)):
#     list1[l[i]][l2[i]][0] = 1
# for i in range(len(list1)):
#     print(list1[i])
# #############################

canvas = paint_canvas(root, size)
# paint_circle(canvas, tuple(list1))

# алгоритм


#########

root.mainloop()
